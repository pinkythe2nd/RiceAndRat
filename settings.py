import os
import pygame
from kivy.utils import platform

path = os.path.dirname(os.path.realpath(__file__))
pygame.init()
if os.path.exists("name.txt"):
    played = True

else:
    played = False

print(platform)

if platform == "win":
    path = f"{path}\\"
    imgpath = f"{path}\\imgs\\"
    soundpath = f"{path}\\soundfx\\"
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    width, height = pygame.display.get_surface().get_size()
    print(width, height)
elif platform == "android":
    path = f"{path}/"
    imgpath = f"{path}/imgs/"
    soundpath = f"{path}/soundfx/"
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
    width, height = pygame.display.get_surface().get_size()
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
else:
    path = f"{path}/"
    imgpath = f"{path}/imgs/"
    soundpath = f"{path}/soundfx/"
    info = pygame.display.Info()
    screen = pygame.display.set_mode((info.current_w, info.current_h))
    width, height = pygame.display.get_surface().get_size()
    width -= 100
    height -= 75
    screen = pygame.display.set_mode((width, height))

running = True
dead = False

#images
player_img = f"{imgpath}chinman.png"
player_img_left = f"{imgpath}chinman_left.png"
food_img = f"{imgpath}molerat.png"
gerbil_img = f"{imgpath}gerbil_chariot.png"
backgroundNight = f"{imgpath}backgroundnight.png"
backgroundDay = f"{imgpath}backgroundday.png"
rockImg = f"{imgpath}rock.png"
fish = f"{imgpath}fosh.png"
skelyfish = f"{imgpath}skelyfish.png"
racoonimg = f"{imgpath}racoon.png"
bossracoon = f"{imgpath}bossracoon.png"
bossracoon2 = f"{imgpath}bossracoon2.png"
explosive = f"{imgpath}explosion.png"

icon = pygame.image.load(f"{imgpath}molerat.png")

#networking
HOST = 'robins.ddns.net'
PORT = 53

#sound effects
deathSound = pygame.mixer.Sound(f"{soundpath}death.wav")
song = pygame.mixer.Sound(f"{soundpath}song.wav")
eaten = pygame.mixer.Sound(f"{soundpath}bite.wav")
clangsfx = pygame.mixer.Sound(f"{soundpath}clang.wav")
explosionsfx = pygame.mixer.Sound(f"{soundpath}explosion.wav")

bgN = pygame.image.load(backgroundNight)
bgD = pygame.image.load(backgroundDay)

FPS = 120

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
purple = (128, 0, 128)

if width == 1920 and height == 1080:
    skelyfishl = pygame.image.load(skelyfish)
    fishl = pygame.image.load(fish)
    widthScale = 1920
    heightScale = 1080
else:
    if width < height:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        width, height = pygame.display.get_surface().get_size()
        width = height
        height = width
        screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

    widthScale = round(1920 / width, 2)
    heightScale = round(1080 / height, 2)

    skelyfishl = pygame.image.load(skelyfish)
    imgwidth = skelyfishl.get_width()
    widthscaled = round(imgwidth / widthScale)
    imgheight = skelyfishl.get_height()
    heightscaled = round(imgheight / heightScale)
    skelyfishl = pygame.transform.scale(skelyfishl, (widthscaled, heightscaled))
    fishl = pygame.image.load(fish)
    imgwidth = fishl.get_width()
    widthscaled = round(imgwidth / widthScale)
    imgheight = fishl.get_height()
    heightscaled = round(imgheight / heightScale)
    fishl = pygame.transform.scale(fishl,(widthscaled, heightscaled))

bgN = pygame.transform.scale(bgN, (width, height))
bgD = pygame.transform.scale(bgD, (width, height))

biggerfont = pygame.font.Font('freesansbold.ttf', 50)
font = pygame.font.Font('freesansbold.ttf', 32)

pygame.display.set_caption("Rice With Meat")

pygame.display.set_icon(icon)

#Groups:
foodList = pygame.sprite.Group()
allSpritesList = pygame.sprite.Group()
racoonlist = pygame.sprite.Group()
BossRacoonlist = pygame.sprite.Group()
projectilelist = pygame.sprite.Group()

clock = pygame.time.Clock()

textWidth = round(width / 2)
hiddenButtonWidth = round(width / 10)
hiddenButtonHeight = round(height / 8)

secondHiddenButtonEndWidth = round(width / 10)
secondHiddenButtonEndWidth += secondHiddenButtonEndWidth 
secondHiddenButtonEndHeight = round(height / 1.2)

secondHiddenButtonStartWidth = round(width / 8)
secondHiddenButtonStartHeight = round(height / 1.5)

