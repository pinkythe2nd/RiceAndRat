import pygame
import json
import ast
import socket
from settings import *
from sprites import *
from levels import level1, level2, level3

class game():
    def __init__(self):
        self.running = True
        pygame.init()
        self.clock = pygame.time.Clock()
        self.gradual = round(1.5 / widthScale)
        pygame.mixer.Sound.play(song, loops=-1)

    def new_game(self):
        self.gradual = 1.4
        self.racoonscore = 0
        self.score = 0
        self.Player = player()
        self.Racoon = racoon()
        Food = food()
        allSpritesList.add(self.Player, self.Racoon ,Food)
        foodList.add(Food)
        racoonlist.add(self.Racoon)
        Food.new_food()
        self.run()

    def run(self):
        self.playing = True
        while self.playing == True:
            self.clock.tick(FPS)
            self.events()
            self.collisions()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if self.racoonscore == 5:
            self.racoonscore = 0
            self.Racoon = racoon()
            racoonlist.add(self.Racoon)
            allSpritesList.add(self.Racoon)

        allSpritesList.update()

    def collisions(self):
        collision_list = pygame.sprite.spritecollide(self.Player, foodList, True)
        racoonCollision = pygame.sprite.spritecollide(self.Player, racoonlist, True)
        for Food in collision_list:
            if self.gradual > 0.8:
                self.gradual -= 0.1
            self.racoonscore += 1
            self.score += 1
            self.Player.speed += self.gradual
            self.Racoon.speed += 0.7
            Food = food()
            Food.new_food()
            foodList.add(Food)
            allSpritesList.add(Food)
        for Racoon in racoonCollision:
            self.Player.collided = True

        if self.Player.collided == True:
            Explosion = explosion2()
            allSpritesList.add(Explosion)
            allSpritesList.draw(screen)
            pygame.mixer.Sound.play(explosionsfx)
            pygame.display.flip()
            pygame.time.wait(1500)
            self.playing = False

    def draw(self):
        screen.fill(white)
        allSpritesList.draw(screen)
        text = font.render(f'Score:{self.score} ', True, (red), (yellow))
        screen.blit(text, (0, 0))
        pygame.display.flip()

    def newplayer(self): 
        textWidth = round(width / 2) - round(width / 10)
        button1 = font.render("play without internet", True, (purple), (red))
        entername = font.render("Enter Your Name!, this will be displayed on the scoreboard!", True, (purple), (red))
        length2long = font.render("Length too long, must be under 20 characters! :)", True, (purple), (red))
        takenName = font.render("Sorry name already taken pick another! :)", True, (purple), (red))
        detectedComma = font.render("Sorry Commas arent allowed :_", True, (purple), (red))
        noserver = font.render("no connection to server, check your internet connection you can carry on ", True, (purple), (red))
        noserver2 = font.render("playing but you wont be able to see the leaderboard until you restart the game", True, (purple), (red))
        noserver3 = font.render("with an  internet connection or try again the server might be busy", True, (purple), (red))
        input_box = pygame.Rect(round(width/2) - 40, 200, 140, 45)
        active = False
        text = ''
        newplayerbool = True
        while newplayerbool == True:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    g.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouse[0] >= textWidth - 50 and mouse[0] <= textWidth + 280 and mouse[1] >= 450 and mouse[1] <= 485:
                        newplayerbool = False
                    if input_box.collidepoint(event.pos):
                        active = True
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            textlength = len(text)
                            if textlength >= 20:
                                screen.blit(length2long, (round(width/2) - 120, 240))
                                pygame.display.flip()
                                pygame.time.wait(3000)
                                text = ''
                            else:
                                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                                    s.settimeout(3)
                                    try:
                                        s.connect((HOST, PORT))
                                        commaText = f"{text}"
                                        transportText = commaText.encode()
                                        s.sendall(transportText)
                                        duplicateCheck = s.recv(1024)
                                        duplicateCheck = duplicateCheck.decode()
                                        print(duplicateCheck)
                                        if duplicateCheck == "False":
                                            f = open("name.txt", "w+")
                                            f.write(text)
                                            f.close()
                                            newplayerbool = False
                                        else:
                                            screen.blit(takenName, (round(width/2) - 120, 280))
                                            pygame.display.flip()
                                            pygame.time.wait(3000)
                                            text = ''
                                    except socket.timeout:
                                        screen.blit(noserver, (0, 240))
                                        screen.blit(noserver2, (0, 280))
                                        screen.blit(noserver3, (0, 320))
                                        pygame.display.flip()
                                        pygame.time.wait(5000)

                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
                screen.blit(bgN, (0, 0))
                screen.blit(button1, (textWidth - 50, 450))
                txt_surface = font.render(text, True, (purple), (red))
                boxwidth = max(190, txt_surface.get_width()+10)
                input_box.w = boxwidth
                screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
                pygame.draw.rect(screen, red, input_box, 2)
                screen.blit(entername, (round(width/2) - 390, 160))
                pygame.display.flip()
        

    def startMenu(self): #this is the first menu the player sees
        screen.blit(bgD, (0, 0)) # blits an image on the screen if passed (0, 0) then the image will fill the screen

        #setting text boxes up
        welcomeMsg = biggerfont.render("Welcome To!", True, (purple), (red))
        gameTitle = biggerfont.render("Rice and Rat!", True, (purple), (red))

        button1 = font.render("Freeplay", True, (purple), (red))
        button2 = font.render("Exit", True, (purple), (red))
        button3 = font.render("Levels", True, (purple), (red))

        textWidth = round(width / 2) - round(width / 10)

        #draw the text boxes at the coordinates 
        screen.blit(welcomeMsg, (textWidth, 100))
        screen.blit(gameTitle, (textWidth, 200))

        screen.blit(button1, (textWidth, 450))
        screen.blit(button2, (textWidth + 150, 450))
        screen.blit(button3, (textWidth + 250, 450))

        pygame.display.flip()#updates the screen
        startMenuBool = True
        fishcheck = False
        while startMenuBool == True: #sets a loop so the game can detect mouse inputs.
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    g.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    #restart button
                    if mouse[0] >= textWidth and mouse[0] <= textWidth + 120 and mouse[1] >= 450 and mouse[1] <= 485:
                        startMenuBool = False

                    #exit button
                    if mouse[0] >= textWidth + 120 and mouse[0] <= textWidth + 220 and mouse[1] >= 450 and mouse[1] <= 485:
                        startMenuBool = False
                        g.running = False

                    #level button
                    if mouse[0] >= textWidth + 220 and mouse[0] <= textWidth + 350 and mouse[1] >= 450 and mouse[1] <= 485:
                        startMenuBool = False
                        self.levelMenu()

                    if mouse[0] >= 0 and mouse[0] <= hiddenButtonWidth and mouse[1] >= 0 and mouse[1] <= hiddenButtonHeight:
                        fishcheck = True

                    if mouse[0] >= secondHiddenButtonStartWidth and mouse[0] <= secondHiddenButtonEndWidth and mouse[1] >= secondHiddenButtonStartHeight and mouse[1] <= secondHiddenButtonEndHeight:
                        fishcheck = False

                screen.blit(bgD, (0, 0))
                screen.blit(welcomeMsg, (textWidth, 100))
                screen.blit(gameTitle, (textWidth, 200))

                screen.blit(button1, (textWidth, 450))
                screen.blit(button2, (textWidth + 150, 450))
                screen.blit(button3, (textWidth + 250, 450))
                rect = fishl.get_rect()
                if fishcheck == False:
                    rect = fishl.get_rect()
                    screen.blit(fishl, (mouse[0]-round(width / 15), mouse[1]-round(height / 15)))
                else:
                    rect = skelyfishl.get_rect()
                    screen.blit(skelyfishl, (mouse[0]-round(width / 15), mouse[1]-round(height / 15)))
                pygame.display.flip()

    def levelMenu(self):
        screen.blit(bgD, (0, 0))
        gameTitle = biggerfont.render("Level Select", True, (purple), (red))

        button1 = font.render("Level 1", True, (purple), (red))
        button2 = font.render("Level 2", True, (purple), (red))
        button3 = font.render("Level 3", True, (purple), (red))
        exitButton = font.render("Exit", True, (purple), (red))
        freeplayButton = font.render("Freeplay", True, (purple), (red))

        textWidth = round(width / 2) - round(width / 10)

        screen.blit(gameTitle, (textWidth, 200))
        screen.blit(button1, (textWidth - 50, 450))
        screen.blit(button2, (textWidth + 75, 450))
        screen.blit(button3, (textWidth + 200, 450))
        screen.blit(exitButton, (textWidth, 600))
        screen.blit(freeplayButton, (textWidth + 150, 600))
        levelMenuBool = True
        pygame.display.flip()
        while levelMenuBool == True:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    g.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    #level 1
                    if mouse[0] >= textWidth - 50 and mouse[0] <= textWidth + 60 and mouse[1] >= 450 and mouse[1] <= 485:
                        levelMenuBool = False
                        level1()
                        self.startMenu()

                    #level 2
                    if mouse[0] >= textWidth + 70 and mouse[0] <= textWidth + 190 and mouse[1] >= 450 and mouse[1] <= 485:
                        levelMenuBool = False
                        level2()
                        self.startMenu()

                    #level 3
                    if mouse[0] >= textWidth + 200 and mouse[0] <= textWidth + 350 and mouse[1] >= 450 and mouse[1] <= 485:
                        levelMenuBool = False
                        level3()
                        self.startMenu()

                    #exit button
                    if mouse[0] >= textWidth and mouse[0] <= textWidth + 70 and mouse[1] >= 600 and mouse[1] <= 635:
                        levelMenuBool = False
                        g.running = False

                    #freeplay Button
                    if mouse[0] >= textWidth + 140 and mouse[0] <= textWidth + 290 and mouse[1] >= 600 and mouse[1] <= 635:
                        levelMenuBool = False

    def game_over_screen(self):
        allSpritesList.empty()
        foodList.empty()
        racoonlist.empty()
        self.gradual = 1.5
        TIMEDOUT = False
        try:
            f = open("score.txt", "r")
            what_in_file = f.read()
            what_in_file = int(what_in_file)
        except FileNotFoundError:
            f = open("score.txt", "w+")
            f.write("0")
            f.close()
            f = open("score.txt", "r")
            what_in_file = f.read()
            what_in_file = int(what_in_file)
            f.close()
        if what_in_file < self.score:
            f = open("score.txt", "w")
            score = str(self.score)
            f.write(score)
            score = int(score)
            f.close()
            try:
                f = open("name.txt", "r")
                name = f.read()
                f.close()
            except FileNotFoundError:
                nonamefile = True
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(3)
                try:
                    print("information on leaederboard")
                    s.connect((HOST, PORT))
                    flag = b"pp,"
                    s.sendall(flag)
                    namescore = {'name': (name), 'score': (score)}
                    namescore = json.dumps(namescore).encode("utf-8")
                    s.sendall(namescore)
                    print("sent better scores")
                    leaderboardstats = s.recv(1024)
                    print(leaderboardstats)
                except socket.timeout:
                    TIMEDOUT = True
        else:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(3)
                try:
                    print("information on leaederboard")
                    s.connect((HOST, PORT))
                    namescore = b","
                    s.sendall(namescore)
                    leaderboardstats = s.recv(1024)
                except socket.timeout:
                    TIMEDOUT = True

        screen.blit(bgN, (0, 0))

        deathmsg = biggerfont.render("you died!!!!", True, (purple), (red))
        scoremsg = font.render(f"Your Score is:{self.score}", True, (purple), (red))
        bestscore = font.render(f"Your Highest Score is:{what_in_file}", True, (purple), (red))
        timedoutmsg = font.render(f"Sorry Highest leaderboards scores arent available.", True, (purple), (red))

        button1 = font.render("Restart", True, (purple), (red))
        button2 = font.render("Exit", True, (purple), (red))
        button3 = font.render("Levels", True, (purple), (red))

        textWidth = round(width / 2) - round(width / 10)

        vertical = 500
        count = 0
        if TIMEDOUT == False:
            leaderboardstatsstr = leaderboardstats.decode("utf-8")
            print(leaderboardstatsstr)
            leaderboardstatsstr = ast.literal_eval(leaderboardstatsstr)
            for iteminlist in leaderboardstatsstr:
                goaway = "{'}"
                iteminlist = str(iteminlist)
                for charachter in goaway:
                    iteminlist = iteminlist.replace(charachter, "")
                print(iteminlist)
                count += 1
                highscores = font.render(f"{count}: {iteminlist}", True, (purple), (red))
                
                screen.blit(highscores, (textWidth, vertical))
                vertical += 50
        else:
            screen.blit(timedoutmsg, (textWidth, 500))
        screen.blit(deathmsg, (textWidth, 100))
        screen.blit(scoremsg, (textWidth, 200))
        screen.blit(bestscore, (textWidth, 300))

        screen.blit(button1, (textWidth, 450))
        screen.blit(button2, (textWidth + 150, 450))
        screen.blit(button3, (textWidth + 250, 450))
        pygame.display.flip()
        game_over = True
        while game_over == True:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    g.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    #restart button
                    if mouse[0] >= textWidth and mouse[0] <= textWidth + 120 and mouse[1] >= 450 and mouse[1] <= 485:
                        game_over = False

                    #exit button
                    if mouse[0] >= textWidth + 120 and mouse[0] <= textWidth + 220 and mouse[1] >= 450 and mouse[1] <= 485:
                        game_over = False
                        g.running = False

                    #level button
                    if mouse[0] >= textWidth + 200 and mouse[0] <= textWidth + 540 and mouse[1] >= 450 and mouse[1] <= 485:
                        game_over = False
                        self.levelMenu()
   
g = game()
if played == True:
    g.startMenu()
else:
    g.newplayer()
g.startMenu()
while g.running == True:
    g.new_game()
    g.game_over_screen()

pygame.quit()
