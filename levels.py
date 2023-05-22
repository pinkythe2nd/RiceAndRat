from settings import *
from sprites import *

def level1(): #level 1 very smiliar code to the normal game 
    gradual = 1.5
    Player = player()
    Food = food()
    allSpritesList.add(Player, Food)
    foodList.add(Food)
    Food.rect.x = round(width / 2) + 200
    Food.rect.y = round(height / 2)
    level1text = font.render("Catch the Naked gangster molerat!", True, (purple), (red))
    level1text2 = font.render("P.S. avoid the dirty racoons and the screens borders", True, (purple), (red))
    level1text3 = font.render("P.P.S. Try Using the arrow Keys! :)", True, (purple), (red))
    level1completetxt = font.render("LEVEL COMPLETE!!!! 0_0", True, (purple), (red))
    level1bool = True
    while level1bool == True: #the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        allSpritesList.update()
        collision_list = pygame.sprite.spritecollide(Player, foodList, True)
        for Food in collision_list:
            level1bool = False

        if Player.collided == True:
            Explosion = explosion2()
            allSpritesList.add(Explosion)
            allSpritesList.draw(screen)
            pygame.mixer.Sound.play(explosionsfx)
            pygame.display.flip()
            pygame.time.wait(1500)
            level1bool = False

        screen.fill(white)
        screen.blit(level1text, (100, 100))
        screen.blit(level1text2, (100, 200))
        screen.blit(level1text3, (100, 300))
        allSpritesList.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()

    if Player.collided == True:
        allSpritesList.empty()
        foodList.empty()
        racoonlist.empty()
    else:
        screen.blit(level1completetxt, (100, 400))
        pygame.display.flip()
        pygame.time.wait(3000)
        allSpritesList.empty()
        foodList.empty()
        racoonlist.empty()

def level2(): #level 2 similar to level 1 but with a score goal to reach to finish the level
    gradual = 1.5
    score = 0
    Player = player()
    Racoon = racoon()
    Food = food()
    allSpritesList.add(Player, Racoon, Food)
    foodList.add(Food)
    racoonlist.add(Racoon)
    Food.new_food()

    level2text1 = font.render("Get 5 mole rats and dont let the racoon get you!", True, (purple), (red))
    level2completetxt = font.render("LEVEL COMPLETE!!!! 0_0", True, (purple), (red))
    level2bool = True
    while level2bool == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if score == 5:
            level2bool = False

        allSpritesList.update()

        collision_list = pygame.sprite.spritecollide(
            Player, foodList, True)
        racoonCollision = pygame.sprite.spritecollide(
            Player, racoonlist, True)
        for Food in collision_list:
            if gradual > 0.8:
                gradual -= 0.1
            score += 1
            Player.speed += gradual
            Racoon.speed += 0.7
            Food = food()
            Food.new_food()
            foodList.add(Food)
            allSpritesList.add(Food)

        for Racoon in racoonCollision:
            Player.collided = True

        if Player.collided == True:
            Explosion = explosion2()
            allSpritesList.add(Explosion)
            allSpritesList.draw(screen)
            pygame.mixer.Sound.play(explosionsfx)
            pygame.display.flip()
            pygame.time.wait(1500)
            level2bool = False

        screen.fill(white)
        allSpritesList.draw(screen)
        text = font.render(f'Score:{score} ', True, (red), (yellow))
        screen.blit(level2text1, (0, 100))
        screen.blit(text, (0, 0))
        clock.tick(FPS)
        pygame.display.flip()

    if Player.collided == True:
        allSpritesList.empty()
        foodList.empty()
        racoonlist.empty()
    else:
        screen.blit(level2completetxt, (100, 400))
        pygame.display.flip()
        pygame.time.wait(3000)
        allSpritesList.empty()
        foodList.empty()
        racoonlist.empty()

def level3(): #level 3 is the most different and hard with a new feature of the player can fire
    gradual = 1.5
    score = 0
    ammo = 0
    racoonscore = 0

    Player = player()
    Racoon = racoon()
    Food = food()
    BossRacoon = boss_racoon()
    BossRacoon2 = bossracoon2sprite()
    Explosion = explosion()

    BossRacoonlist.add(BossRacoon)
    allSpritesList.add(Player, Racoon, Food, BossRacoon)

    foodList.add(Food)
    racoonlist.add(Racoon)
    Food.new_food()


    level3text1 = font.render("Get 8 mole rats and poop a rock on the boss!", True, (purple), (red))
    level3completetxt = font.render("LEVEL COMPLETE!!!! 0_0", True, (purple), (red))
    level3bool = True
    while level3bool == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                if ammo == 1:
                    Projectile = projectile()
                    Projectile.direction()
                    allSpritesList.add(Projectile)
                    projectilelist.add(Projectile)
                    ammo -= 1

        if score == 8:
            ammo += 1
            score = 0

        allSpritesList.update()

        if racoonscore == 2:
            racoonscore = 0
            Racoon = racoon()
            racoonlist.add(Racoon)
            allSpritesList.add(Racoon)

        collision_list = pygame.sprite.spritecollide(Player, foodList, True)
        racoonCollision = pygame.sprite.spritecollide(Player, racoonlist, True)
        projectileCollision = pygame.sprite.spritecollide(BossRacoon, projectilelist, True)
        moleratCollision = pygame.sprite.spritecollide(BossRacoon, foodList, True)
        playerCollision = pygame.sprite.spritecollide(Player, BossRacoonlist, True)

        for Food in collision_list:
            if gradual > 0.8:
                gradual -= 0.1
            score += 1
            racoonscore += 1
            Player.speed += gradual
            Racoon.speed += 0.7
            Food = food()
            Food.new_food()
            foodList.add(Food)
            allSpritesList.add(Food)

        for BossRacoon in moleratCollision:
            Food = food()
            Food.new_food()
            foodList.add(Food)
            allSpritesList.add(Food)

        for Player in playerCollision:
            Player.collided = True

        for Racoon in racoonCollision:
            Player.collided = True

        for BossRacoon in projectileCollision:
            level3bool = False

        if Player.collided == True:
            Explosion = explosion2()
            allSpritesList.add(Explosion)
            allSpritesList.draw(screen)
            pygame.mixer.Sound.play(explosionsfx)
            pygame.display.flip()
            pygame.time.wait(1500)
            level3bool = False
        
        screen.fill(white)
        allSpritesList.draw(screen)
        text = font.render(f'Score:{score} ', True, (red), (yellow))
        text2 = font.render(f'ammo:{ammo} ', True, (red), (yellow))
        screen.blit(level3text1, (0, 150))
        screen.blit(text, (0, 0))
        screen.blit(text2, (0, 100))
        clock.tick(FPS)
        pygame.display.flip()

    if Player.collided == True:
        allSpritesList.empty()
        foodList.empty()
        racoonlist.empty()
    else:
        screen.blit(level3completetxt, (100, 400))
        allSpritesList.remove(BossRacoon)
        allSpritesList.add(BossRacoon2)
        allSpritesList.draw(screen)
        pygame.display.flip()
        pygame.time.wait(2000)
        allSpritesList.remove(BossRacoon2)
        allSpritesList.add(Explosion)
        allSpritesList.draw(screen)
        pygame.mixer.Sound.play(explosionsfx)
        pygame.display.flip()
        pygame.time.wait(3000)
        allSpritesList.empty()
        foodList.empty()
        racoonlist.empty()
        BossRacoonlist.empty()
