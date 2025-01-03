import pygame, sys

from Assets.Settings import *
from Assets.Background import background
from Assets.Player import player
from Assets.Door import door
from Assets.Blocks import blocks

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.NOFRAME)
        pygame.display.set_caption('Pygame_SN')
        self.clock = pygame.time.Clock()

    def eventListener(self):
        for event in pygame.event.get():
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_ESCAPE] :
                pygame.quit()
                sys.exit()

            # move left
            if key_pressed[pygame.K_LEFT] and not player.ismoving:
                player.dirrection = {key: False for key in player.dirrection}
                player.dirrection['left'] = True

            # move right
            if key_pressed[pygame.K_RIGHT] and not player.ismoving:
                player.dirrection = {key: False for key in player.dirrection}
                player.dirrection['right'] = True

            # jump
            if key_pressed[pygame.K_UP] and not player.isjumping:
                player.isjumping = True
                player.jump()

            # player.ismoving status
            if key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_RIGHT]:
                player.ismoving = True
            if not key_pressed[pygame.K_LEFT] and not key_pressed[pygame.K_RIGHT]:
                player.ismoving = False
            if key_pressed[pygame.K_LEFT] and key_pressed[pygame.K_RIGHT]:
                player.ismoving = False

    def drawScreen(self):
        self.screen.fill(BG_COLOR)

        background.draw(self.screen)
        door.draw(self.screen)
        blocks.draw(self.screen)

        # for i in background.tiles.lists.keys():
        #     for j in background.tiles.lists[i]:
        #         pygame.draw.rect(self.screen,'white',j, 1)
            
        # playerrect = player.image.get_rect(topleft=(player.x,player.y))
        # pygame.draw.rect(self.screen,'red',playerrect)
    
        # pygame.draw.rect(self.screen,'blue',player.hitbox.mainRect,1)
        # pygame.draw.rect(self.screen,'green',player.hitbox.leftRect,1)
        # pygame.draw.rect(self.screen,'yellow',player.hitbox.rightRect,1)
        # pygame.draw.rect(self.screen,'red',player.hitbox.topRect,1)
        # pygame.draw.rect(self.screen,'white',player.hitbox.bottomRect,1)

        player.draw(self.screen)

    def run(self):
        while True:
            self.clock.tick(FPS)
            self.eventListener()

            background.update(player)
            player.update()
            blocks.update()
            door.update()

            self.drawScreen()
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()
