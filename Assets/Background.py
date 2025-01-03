import pygame, os

from Assets.Settings import *

class CollitionBox:
    def __init__(self):
        self.currentLevel = 'level1'
        self.datas = {
            1 : 'floorBlocks',
            2 : 'platformUpPass',
            3 : 'platformDownPass',
            4 : 'box',
            5 : 'blockEnemy',
            6 : 'door'
        }
        self.levels = {
            'level1': {
                'spawnPoint': (200,400),
                'verticalBlocks': 8,
                'horizontalBlocks': 15,
                'size': (1,1),
                'data':[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,1,1,1,1,1,1,1,1,1,1,0],
                        [0,1,1,1,0,0,0,0,0,0,0,0,0,1,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,1,0,4,0,0,0,0,0,4,0,6,0,1,0],
                        [0,1,1,1,0,0,0,0,4,1,1,1,1,1,0],
                        [0,0,0,1,1,1,1,1,1,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
            },

            'level2': {
                'spawnPoint': (200,400),
                'verticalBlocks': 8,
                'horizontalBlocks': 15,
                'size': (1,1),
                'data':[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,1,1,1,0,1,1,1,1,1,1,0],
                        [0,1,1,1,0,0,1,1,1,0,0,0,0,1,0],
                        [0,1,0,0,0,0,1,0,0,0,0,0,0,1,0],
                        [0,1,0,0,0,0,0,0,0,1,0,6,0,1,0],
                        [0,1,0,0,1,0,0,0,5,1,1,1,1,1,0],
                        [0,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
            },

            'level3': {
                'spawnPoint': (300,250),
                'verticalBlocks': 8,
                'horizontalBlocks': 15,
                'size': (1,1),
                'data':[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                        [0,1,0,0,1,0,0,0,0,1,0,0,0,1,0],
                        [0,1,0,0,1,0,2,1,0,1,6,0,0,1,0],
                        [0,1,0,2,2,2,1,1,0,1,3,3,0,1,0],
                        [0,1,4,0,0,5,1,0,0,0,0,0,2,1,0],
                        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
            },

            'level4': {
                'spawnPoint': (1100,300),
                'verticalBlocks': 16,
                'horizontalBlocks': 15,
                'size': (1,2),
                'data':[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                        [0,1,0,0,0,0,1,1,0,0,0,0,0,1,0],
                        [0,1,0,6,0,0,1,1,0,0,4,0,0,1,0],
                        [0,1,2,1,1,3,0,0,0,0,1,1,1,1,0],
                        [0,1,0,0,1,0,1,0,0,2,2,0,0,1,0],
                        [0,1,5,0,0,2,1,0,0,0,0,0,0,1,0],
                        [0,1,1,1,1,2,1,1,2,0,0,1,1,1,0],
                        [0,1,1,1,0,0,1,0,0,0,0,0,1,1,0],
                        [0,1,1,0,0,5,1,1,5,0,0,0,0,1,0],
                        [0,1,2,2,2,2,2,1,1,3,3,1,0,1,0],
                        [0,1,0,5,0,0,0,0,1,0,0,1,0,1,0],
                        [0,1,3,1,2,0,0,0,1,1,1,1,3,1,0],
                        [0,1,0,0,0,5,0,0,0,0,0,0,0,1,0],
                        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
            }
        }

class Tiles:
    def __init__(self, collitionbox):
        self.collitionbox = collitionbox
        self.width = (self.collitionbox.levels[self.collitionbox.currentLevel]['size'][0] * WINDOW_WIDTH) / self.collitionbox.levels[self.collitionbox.currentLevel]['horizontalBlocks']
        self.height = (self.collitionbox.levels[self.collitionbox.currentLevel]['size'][1] * WINDOW_HEIGHT) / self.collitionbox.levels[self.collitionbox.currentLevel]['verticalBlocks']
        self.lists = {
            'floorBlocks': [],
            'platformUpPass': [],
            'platformDownPass': [],
            'box': [],
            'blockEnemy': [],
            'door': []
        }

    def create_rect(self):
        for row_idx, row in enumerate(self.collitionbox.levels[self.collitionbox.currentLevel]['data']):
            for col_idx, col in enumerate(row):
                if col in self.collitionbox.datas.keys():
                    rect = pygame.Rect(self.width * col_idx, self.height * row_idx, self.width, self.height)

                    # platforms
                    if self.collitionbox.datas[col] == 'platformUpPass':
                        rect = self.adjustRect(rect, 2,2,-2,-82)
                        self.lists['platformUpPass'].append(rect)
                    if self.collitionbox.datas[col] == 'platformDownPass':
                        rect = self.adjustRect(rect, 2,0,0,-90)
                        self.lists['platformDownPass'].append(rect) 

                    # blockEnemy
                    if self.collitionbox.datas[col] == 'blockEnemy':
                        rect = self.adjustRect(rect, 15,32,-30,-32)
                        self.lists['blockEnemy'].append(rect)

                    # blockBox
                    if self.collitionbox.datas[col] == 'box':
                        rect = self.adjustRect(rect, 19,68,-38,-68)
                        self.lists['box'].append(rect)

                    # door    
                    if self.collitionbox.datas[col] == 'door':
                        rect = self.adjustRect(rect, 70,0,-50,0)
                        self.lists['door'].append(rect)

                    # floorBlocks
                    if (self.collitionbox.datas[col] == 'floorBlocks'):
                        rect = self.adjustRect(rect, 2,0,0,-2)
                        self.lists['floorBlocks'].append(rect)

    def adjustRect(self, rect, x, y, width, height):
        rect.x += x 
        rect.y += y
        rect.width += width
        rect.height += height
        return rect
    
    def reset(self):
        self.width = (self.collitionbox.levels[self.collitionbox.currentLevel]['size'][0] * WINDOW_WIDTH) / self.collitionbox.levels[self.collitionbox.currentLevel]['horizontalBlocks']
        self.height = (self.collitionbox.levels[self.collitionbox.currentLevel]['size'][1] * WINDOW_HEIGHT) / self.collitionbox.levels[self.collitionbox.currentLevel]['verticalBlocks']
        self.lists = {key:[] for key in self.lists}
        self.create_rect()

class Background :
    def __init__(self, collitionbox, tiles):
        self.collitionbox = collitionbox
        self.tiles = tiles

        self.x = self.y = 0
        self.width = self.collitionbox.levels[self.collitionbox.currentLevel]['size'][0] * WINDOW_WIDTH
        self.height = self.collitionbox.levels[self.collitionbox.currentLevel]['size'][1] * WINDOW_HEIGHT
        self.tiles.create_rect()
        self.boundary = 200

        self.image = pygame.transform.scale(
            pygame.image.load(os.path.join('.', 'Assets', 'Images', 'Levels', self.collitionbox.currentLevel + '.png')),
            tuple(x * y for x, y in zip(self.collitionbox.levels[self.collitionbox.currentLevel]['size'], (WINDOW_WIDTH, WINDOW_HEIGHT))))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self, player):
        # move bg up if player goes down
        if player.hitbox.mainRect.y + player.hitbox.mainRect.height > WINDOW_HEIGHT-self.boundary and self.y+self.height > WINDOW_HEIGHT and player.velocity_y > 0 :
            self.y -= player.velocity_y
            player.y -= player.velocity_y

            for tile in self.tiles.lists:
                for rect in self.tiles.lists[tile]:
                    rect.y -= player.velocity_y

        # move bg down if player goes up
        if player.hitbox.mainRect.y < self.boundary and self.y < 0 and player.velocity_y < 0:
            self.y -= player.velocity_y
            player.y -= player.velocity_y

            for tile in self.tiles.lists:
                for rect in self.tiles.lists[tile]:
                    rect.y -= player.velocity_y

    def changeLevel(self):
        self.getNextLevel()
        self.image = pygame.transform.scale(
            pygame.image.load(os.path.join('.', 'Assets', 'Images', 'Levels', self.collitionbox.currentLevel + '.png')),
            tuple(x * y for x, y in zip(self.collitionbox.levels[self.collitionbox.currentLevel]['size'], (WINDOW_WIDTH, WINDOW_HEIGHT))))
        self.tiles.reset()
        self.x = self.y = 0
        self.width = self.collitionbox.levels[self.collitionbox.currentLevel]['size'][0] * WINDOW_WIDTH
        self.height = self.collitionbox.levels[self.collitionbox.currentLevel]['size'][1] * WINDOW_HEIGHT

    def getNextLevel(self):
        maxLevel = len(self.collitionbox.levels)
        currentLvl = int(self.collitionbox.currentLevel[-1])
        self.collitionbox.currentLevel = 'level'+ str(currentLvl + 1) if currentLvl < maxLevel else 'level1' 

collitionbox = CollitionBox()
tiles = Tiles(collitionbox = collitionbox)
background = Background(collitionbox = collitionbox, 
                        tiles = tiles)   

