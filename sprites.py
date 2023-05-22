import pygame
import random
from settings import *

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        if width == 1920 and height == 1080:
            self.image = pygame.image.load(player_img)
            self.speed = 2
        else:
            self.image = pygame.image.load(player_img)
            imgwidth = self.image.get_width()
            widthscaled = round(imgwidth / widthScale)
            imgheight = self.image.get_height()
            heightscaled = round(imgheight / heightScale)
            self.image = pygame.transform.scale(self.image, (widthscaled, heightscaled))
            self.speed = round(2 / widthScale, 1)

        self.rect = self.image.get_rect()
        self.velocity_x = 0
        self.velocity_y = 0
        self.collided = False
        self.rect.x = round(width / 2)
        self.rect.y = round(height / 2)

    def update(self):
        global facing
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            facing = -1
            if width == 1920 and height == 1080:
                self.image = pygame.image.load(player_img_left)
            else:
                self.image = pygame.image.load(player_img_left)
                imgwidth = self.image.get_width()
                widthscaled = round(imgwidth / widthScale)
                imgheight = self.image.get_height()
                heightscaled = round(imgheight / heightScale)
                self.image = pygame.transform.scale(self.image, (widthscaled, heightscaled))

            self.velocity_x =- self.speed
            self.velocity_y = 0
        if keys[pygame.K_RIGHT]:
            facing = 1
            if width == 1920 and height == 1080:
                self.image = pygame.image.load(player_img)
            else:
                self.image = pygame.image.load(player_img)
                imgwidth = self.image.get_width()
                widthscaled = round(imgwidth / widthScale)
                imgheight = self.image.get_height()
                heightscaled = round(imgheight / heightScale)
                self.image = pygame.transform.scale(self.image, (widthscaled, heightscaled))
            self.velocity_x = self.speed
            self.velocity_y = 0
        if keys[pygame.K_UP]:
            self.velocity_y =- self.speed
            self.velocity_x = 0
        if keys[pygame.K_DOWN]:
            self.velocity_y = self.speed
            self.velocity_x = 0

        if self.rect.right > width:
            self.rect.right = width
            self.collided = True
        if self.rect.left < 0:
            self.rect.left = 0
            self.collided = True
        if self.rect.bottom > height:
            self.rect.bottom = height
            self.collided = True
        if self.rect.top < 0:
            self.rect.top = 0
            self.collided = True

        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        global px
        global py
        global pcenter
        px = self.rect.x
        py = self.rect.y
        pcenter = self.rect.center

class food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        if width == 1920 and height == 1080:
            self.image = pygame.image.load(food_img)
        else:
            self.image = pygame.image.load(food_img)
            imgwidth = self.image.get_width()
            widthscaled = round(imgwidth / widthScale)
            imgheight = self.image.get_height()
            heightscaled = round(imgheight / heightScale)
            self.image = pygame.transform.scale(self.image, (widthscaled, heightscaled))
        self.rect = self.image.get_rect()

    def new_food(self):
        pygame.mixer.Sound.play(eaten)
        self.rect.x = random.randrange(width)
        self.rect.y = random.randrange(height)

        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > height:
            self.rect.bottom = height
        if self.rect.top < 0:
            self.rect.top = 0


class racoon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        if width == 1920 and height == 1080:
            self.image = pygame.image.load(racoonimg)
            self.speed = 2
        else:
            self.image = pygame.image.load(racoonimg)
            imgwidth = self.image.get_width()
            widthscaled = round(imgwidth / widthScale)
            imgheight = self.image.get_height()
            heightscaled = round(imgheight / heightScale)
            self.image = pygame.transform.scale(
                self.image, (widthscaled, heightscaled))
            self.speed = round(2 / widthScale, 1)
        self.rect = self.image.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y

    def update(self):
        dirvect = pygame.math.Vector2(px - self.rect.x,
                                      py - self.rect.y)
        dirvect.normalize()
        dirvect.scale_to_length(self.speed)
        self.rect.move_ip(dirvect)

class boss_racoon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        if width == 1920 and height == 1080:
            self.image = pygame.image.load(bossracoon)
        else:
            self.image = pygame.image.load(bossracoon)
            imgwidth = self.image.get_width()
            widthscaled = round(imgwidth / widthScale)
            imgheight = self.image.get_height()
            heightscaled = round(imgheight / heightScale)
            self.image = pygame.transform.scale(self.image, (widthscaled, heightscaled))
        self.rect = self.image.get_rect()
        self.rect.x = round(width / 1.2)
        self.rect.y = round(height / 2)

class bossracoon2sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        if width == 1920 and height == 1080:
            self.image = pygame.image.load(bossracoon2)
        else:
            self.image = pygame.image.load(bossracoon2)
            imgwidth = self.image.get_width()
            widthscaled = round(imgwidth / widthScale)
            imgheight = self.image.get_height()
            heightscaled = round(imgheight / heightScale)
            self.image = pygame.transform.scale(
                self.image, (widthscaled, heightscaled))
        self.rect = self.image.get_rect()
        self.rect.x = round(width / 1.2)
        self.rect.y = round(height / 2)
        global bossRacoonCenter
        bossRacoonCenter = self.rect.center

class explosion(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        if width == 1920 and height == 1080:
            self.image = pygame.image.load(explosive)
        else:
            self.image = pygame.image.load(explosive)
            imgwidth = self.image.get_width()
            widthscaled = round(imgwidth / widthScale)
            imgheight = self.image.get_height()
            heightscaled = round(imgheight / heightScale)
            self.image = pygame.transform.scale(self.image, (widthscaled, heightscaled))
        self.rect = self.image.get_rect()
        self.rect.center = bossRacoonCenter


class explosion2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        if width == 1920 and height == 1080:
            self.image = pygame.image.load(explosive)
        else:
            self.image = pygame.image.load(explosive)
            imgwidth = self.image.get_width()
            widthscaled = round(imgwidth / widthScale)
            imgheight = self.image.get_height()
            heightscaled = round(imgheight / heightScale)
            self.image = pygame.transform.scale(
                self.image, (widthscaled, heightscaled))
        self.rect = self.image.get_rect()
        self.rect.center = pcenter


class projectile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity_x = 0
        if width == 1920 and height == 1080:
            self.image = pygame.image.load(rockImg)
        else:
            self.image = pygame.image.load(rockImg)
            imgwidth = self.image.get_width()
            widthscaled = round(imgwidth / widthScale)
            imgheight = self.image.get_height()
            heightscaled = round(imgheight / heightScale)
            self.image = pygame.transform.scale(self.image, (widthscaled, heightscaled))
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
    
    def direction(self):
        if facing == -1:
            self.velocity_x =- 5
            #go left
        else:
            self.velocity_x =+ 5
        self.update()

    def update(self):
        self.rect.x += self.velocity_x
        
