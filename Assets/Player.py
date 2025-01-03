import pygame, os

from Assets.Settings import *
from Assets.Animation import Animation
from Assets.Background import background

class Player:
    def __init__(self, hitbox):
        self.hitbox = hitbox
        self.animatePlayer = Animation()

        self.x, self.y = background.collitionbox.levels[background.collitionbox.currentLevel]['spawnPoint']
        self.velocity_y = 0

        self.ismoving = False
        self.isjumping = False
        self.changingLevel = False
        self.dirrection = {
            "left": False,
            "right": True
        }

        self.image = None
        self.spriteSheets = {
            'idle': {
                'image': pygame.transform.scale_by(pygame.image.load(os.path.join('.','Assets','Images','Player','idle.png')),3),
                'totalFrames': 11,
                'frameRate': 40
            },

            'run': {
                'image': pygame.transform.scale_by(pygame.image.load(os.path.join('.','Assets','Images','Player','run.png')),3),
                'totalFrames': 8,
                'frameRate': 60
            },

            'enterDoor': {
                'image': pygame.transform.scale_by(pygame.image.load(os.path.join('.','Assets','Images','Player','enterDoor.png')),3),
                'totalFrames': 14,
                'frameRate': 100
            }
        }

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.animation()
        self.horizontal_movement()
        self.vertical_movement()
        self.hitbox.update()

    def animation(self):
        if not self.changingLevel:
            if not self.ismoving:
                if self.dirrection['left']:
                    self.image = self.animatePlayer(
                        self.spriteSheets['idle']['image'],
                        self.spriteSheets['idle']['frameRate'],
                        self.spriteSheets['idle']['totalFrames'],
                        self.spriteSheets['idle']['image'].get_width()/self.spriteSheets['idle']['totalFrames'],
                        self.spriteSheets['idle']['image'].get_height()
                    )
                    self.image = pygame.transform.flip(self.image,True,False)

                if self.dirrection['right']:
                    self.image = self.animatePlayer(
                        self.spriteSheets['idle']['image'],
                        self.spriteSheets['idle']['frameRate'],
                        self.spriteSheets['idle']['totalFrames'],
                        self.spriteSheets['idle']['image'].get_width()/self.spriteSheets['idle']['totalFrames'],
                        self.spriteSheets['idle']['image'].get_height()
                    )
                    
            if self.ismoving:
                if self.dirrection['left']:
                    self.image = self.animatePlayer(
                        self.spriteSheets['run']['image'],
                        self.spriteSheets['run']['frameRate'],
                        self.spriteSheets['run']['totalFrames'],
                        self.spriteSheets['run']['image'].get_width()/self.spriteSheets['run']['totalFrames'],
                        self.spriteSheets['run']['image'].get_height()
                    )
                    self.image = pygame.transform.flip(self.image,True,False)

                if self.dirrection['right']:
                    self.image = self.animatePlayer(
                        self.spriteSheets['run']['image'],
                        self.spriteSheets['run']['frameRate'],
                        self.spriteSheets['run']['totalFrames'],
                        self.spriteSheets['run']['image'].get_width()/self.spriteSheets['run']['totalFrames'],
                        self.spriteSheets['run']['image'].get_height()
                    )
                
        if self.changingLevel:
            self.image = self.animatePlayer(
                self.spriteSheets['enterDoor']['image'],
                self.spriteSheets['enterDoor']['frameRate'],
                self.spriteSheets['enterDoor']['totalFrames'],
                self.spriteSheets['enterDoor']['image'].get_width() / self.spriteSheets['enterDoor']['totalFrames'],
                self.spriteSheets['enterDoor']['image'].get_height(),
                LOOP=False
            )

    def horizontal_movement(self):
        if not self.changingLevel:
            if self.ismoving:
                if self.dirrection.get('left'):
                    self.hitbox.leftRect.x -= PLAYER_SPEED
                    if not any(self.hitbox.leftRect.colliderect(tile) for tile in background.tiles.lists['floorBlocks']) and \
                    not any(self.hitbox.leftRect.colliderect(tile) for tile in background.tiles.lists['blockEnemy']) and \
                    not any(self.hitbox.leftRect.colliderect(tile) for tile in background.tiles.lists['box']):
                        self.x -= PLAYER_SPEED

                if self.dirrection.get('right'):
                    self.hitbox.rightRect.x += PLAYER_SPEED
                    if not any(self.hitbox.rightRect.colliderect(tile) for tile in background.tiles.lists['floorBlocks']) and \
                    not any(self.hitbox.rightRect.colliderect(tile) for tile in background.tiles.lists['blockEnemy']) and \
                    not any(self.hitbox.rightRect.colliderect(tile) for tile in background.tiles.lists['box']):
                        self.x += PLAYER_SPEED

    def vertical_movement(self):
        if not self.changingLevel:

            self.hitbox.bottomRect.y += self.velocity_y
            self.hitbox.topRect.y -= self.velocity_y

            if not any(self.hitbox.bottomRect.colliderect(tile) for tile in background.tiles.lists['floorBlocks']) and \
            not (any(self.hitbox.bottomRect.colliderect(tile) for tile in background.tiles.lists['platformUpPass']) and self.velocity_y>0) and \
            not any(self.hitbox.bottomRect.colliderect(tile) for tile in background.tiles.lists['blockEnemy']) and \
            not any(self.hitbox.bottomRect.colliderect(tile) for tile in background.tiles.lists['box']):
                self.y += self.velocity_y
                self.velocity_y += GRAVITY
            else:
                self.velocity_y = 0
                self.isjumping = False

            if (any(self.hitbox.topRect.colliderect(tile) for tile in background.tiles.lists['floorBlocks']) or
            any(self.hitbox.topRect.colliderect(tile) for tile in background.tiles.lists['platformDownPass'])) and self.velocity_y < 0:
                self.velocity_y = 0                    


    def jump(self):
        if not self.changingLevel:
            self.hitbox.bottomRect.height += 10
            if any(self.hitbox.bottomRect.colliderect(tile) for tile in background.tiles.lists['floorBlocks']) or \
            any(self.hitbox.bottomRect.colliderect(tile) for tile in background.tiles.lists['platformUpPass']) or \
            any(self.hitbox.bottomRect.colliderect(tile) for tile in background.tiles.lists['box']):
                self.velocity_y = -JUMP_HEIGHT
            if any(self.hitbox.bottomRect.colliderect(tile) for tile in background.tiles.lists['blockEnemy']):
                self.velocity_y = -BOOST_JUMP

    def reset(self):
        self.x, self.y = background.collitionbox.levels[background.collitionbox.currentLevel]['spawnPoint']
        self.changingLevel = False
        self.velocity_y = 0

class HitBox:
    def __init__(self):
        self.mainRect = pygame.Rect(0,0,0,0)
        self.leftRect = self.mainRect.copy()
        self.rightRect = self.mainRect.copy()
        self.topRect = self.mainRect.copy()
        self.bottomRect = self.mainRect.copy()

    def update(self):
        self.updateMainRect()
        self.updateLeftRect()
        self.updateRightRect()
        self.updateTopRect()
        self.updateBottomRect()

    def updateMainRect(self):
        self.mainRect.x = player.x+player.image.get_width()*0.15
        self.mainRect.y = player.y+player.image.get_height()*0.12
        self.mainRect.width = player.image.get_width()*0.7
        self.mainRect.height = player.image.get_height()*0.8
    
    def updateLeftRect(self):
        self.leftRect = self.mainRect.copy()
        self.leftRect.width = self.mainRect.width*0.1
        self.leftRect.y += self.mainRect.height*0.05
        self.leftRect.height = self.mainRect.height*0.9

    def updateRightRect(self):
        self.rightRect = self.mainRect.copy()
        self.rightRect.x += self.mainRect.width - self.mainRect.width*0.1
        self.rightRect.width = self.mainRect.width*0.1
        self.rightRect.y += self.mainRect.height*0.05
        self.rightRect.height = self.mainRect.height*0.9

    def updateTopRect(self):
        self.topRect = self.mainRect.copy()
        self.topRect.height = self.mainRect.height*0.3
        self.topRect.x += self.mainRect.width*0.1
        self.topRect.width = self.mainRect.width*0.8

    def updateBottomRect(self):
        self.bottomRect = self.mainRect.copy()
        self.bottomRect.y += self.mainRect.height - self.mainRect.height*0.1
        self.bottomRect.height = self.mainRect.height*0.1
        self.bottomRect.x += self.mainRect.width*0.2
        self.bottomRect.width = self.mainRect.width*0.6

hitbox = HitBox()
player = Player(hitbox)    
