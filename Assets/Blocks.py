import pygame, os

from Assets.Settings import *
from Assets.Animation import Animation
from Assets.Background import background

class Blocks:
    def __init__(self, box, blockenemy):
        self.childs = {
            "box": box,
            "blockenemy": blockenemy
        }

    def draw(self, screen):
        for child in self.childs:
            self.childs[child].draw(screen)

    def update(self):
        for child in self.childs:
            self.childs[child].update()

class Box(Blocks):
    def __init__(self):
        self.animateBox = Animation()
        self.spriteSheet = {
            "idle": {
                'image': pygame.transform.scale_by(pygame.image.load(os.path.join('.','Assets','Images','Box','idle.png')),3),
                'totalFrames': 1,
                'frameRate': 0
            },
        }
        self.image = None

    def draw(self, screen):
        for i in background.tiles.lists['box']:
            screen.blit(self.image, 
                        (i.centerx-self.image.get_width()/2, i.top))
    
    def update(self):
        self.animation()

    def animation(self):
        self.image = self.animateBox(
            self.spriteSheet['idle']['image'],
            self.spriteSheet['idle']['frameRate'],
            self.spriteSheet['idle']['totalFrames'],
            self.spriteSheet['idle']['image'].get_width()/self.spriteSheet['idle']['totalFrames'],
            self.spriteSheet['idle']['image'].get_height()
            )

class BlockEnemy(Blocks):
    def __init__(self):
        self.animateBlockEnemy = Animation()
        self.spriteSheet = {
            "idle": {
                'image': pygame.transform.scale_by(pygame.image.load(os.path.join('.','Assets','Images','Enemy','Block','idle.png')),3),
                'totalFrames': 9,
                'frameRate': 60
            },
        }
        self.image = None

    def draw(self, screen):
        for i in background.tiles.lists['blockEnemy']:
            screen.blit(self.image, 
                        (i.centerx-self.image.get_width()/2, i.bottom-self.image.get_height()))
    
    def update(self):
        self.animation()

    def animation(self):
        self.image = self.animateBlockEnemy(
            self.spriteSheet['idle']['image'],
            self.spriteSheet['idle']['frameRate'],
            self.spriteSheet['idle']['totalFrames'],
            self.spriteSheet['idle']['image'].get_width()/self.spriteSheet['idle']['totalFrames'],
            self.spriteSheet['idle']['image'].get_height()
            )

box = Box()
blockenemy = BlockEnemy()
blocks = Blocks(box = box, 
                blockenemy = blockenemy)