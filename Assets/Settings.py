import pygame
pygame.init()

# colors
BG_COLOR = (63, 56, 81)
BLACK = (0,0,0)
WHITE = (255,255,255)

# main.py
FPS = 60
WINDOW_WIDTH = pygame.display.Info().current_w
WINDOW_HEIGHT = pygame.display.Info().current_h

# Player.py
PLAYER_SPEED = 6
GRAVITY = 2
JUMP_HEIGHT = 22
BOOST_JUMP = 33

# Door.py
LEVELCHANGETIME = 1.5 #sec