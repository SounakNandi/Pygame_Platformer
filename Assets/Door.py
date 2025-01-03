import pygame, os

from Assets.Settings import *
from Assets.Animation import Animation
from Assets.Background import background
from Assets.Player import player

class Door:
    def __init__(self):
        self.animateDoor = Animation()
        self.spriteSheet = {
            'idle': {
                'image': pygame.transform.scale_by(pygame.image.load(os.path.join('.','Assets','Images','Door','idle.png')),2.6),
                'totalFrames': 1,
                'frameRate': 0
            },
            'opening': {
                'image': pygame.transform.scale_by(pygame.image.load(os.path.join('.','Assets','Images','Door','opening.png')),2.5),
                'totalFrames': 5,
                'frameRate': 200
            }
        } 
        self.state = 'idle'
        self.levelOver = False
        self.image = self.spriteSheet[self.state]['image']
        self.startTime = None

    def draw(self, screen):
        for i in background.tiles.lists['door']:
            screen.blit(self.image, 
                        (i.centerx-self.image.get_width()/2, i.bottom-self.image.get_height()))
    
    def update(self):
        self.animation()
        self.check()
        self.changeLevel()

    def animation(self):
        self.image = self.animateDoor(
            self.spriteSheet[self.state]['image'],
            self.spriteSheet[self.state]['frameRate'],
            self.spriteSheet[self.state]['totalFrames'],
            self.spriteSheet[self.state]['image'].get_width()/self.spriteSheet[self.state]['totalFrames'],
            self.spriteSheet[self.state]['image'].get_height(),
            LOOP=False
        )

    def check(self):
        if not self.levelOver:
            for tile in background.tiles.lists['door']:
                if player.hitbox.mainRect.colliderect(tile) and player.velocity_y >= 0:
                    self.levelOver = True
                    self.state = 'opening'
                    self.animateDoor.reset()

                    player.changingLevel = True
                    player.animatePlayer.reset()
                    player.x, player.y = tile.centerx-player.image.get_width() * 0.6, tile.bottom-player.image.get_height() * 1.35
                    self.startTime = pygame.time.get_ticks()
                    self.changeLevel()

    def changeLevel(self):
        if self.levelOver:
            if pygame.time.get_ticks() - self.startTime > LEVELCHANGETIME*1000:
                self.reset()
                background.changeLevel()
                player.reset()

    def reset(self):
        self.levelOver = False
        self.state = 'idle'
        self.animateDoor.reset()

door = Door()