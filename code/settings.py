import pygame
from sys import exit
from os.path import join

#windows
CELL_SIZE = 80
ROWS = 10
COLS = 16
WINDOW_WIDTH = COLS * CELL_SIZE
WINDOW_HEIGHT = ROWS * CELL_SIZE

# colors
LIGHT_GREEN = '#aad751'
DARK_GREEN = '#a2d149'

# Start Pos
START_LENGHT = 3
START_ROW = ROWS // 2
START_COL = START_LENGHT + 2

# shadow
SHADOW_SIZE = pygame.Vector2(4,4)
SHADOW_OPACITY = 50