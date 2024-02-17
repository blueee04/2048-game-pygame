import json
import sys
import time

from copy import deepcopy

import pygame
from pygame.locals import *

from gamelogic import *

pygame.init()
const = json.load(open('const.json'))
screen = pygame.display.set_mode((const['size'], const['size']))
font = pygame.font.SysFont(const["font"], const["fontSize"], bold=True)
BLUE = (0, 0, 255)

def WinCheck(board,status,theme,text):
    if status == "YOU WON":
        text = font.render("YOU WON", True, (255, 255, 255))
        screen.blit(text, (const['width']//2-const['fontSize'], const['height']//2-const['font_size']))
        pygame.display.flip()
        time.sleep(2)
        return True
    return False

def newGame(theme, text):
    board = [[0]*4 for _ in range(4)]
    screen.blit(font.render(text, True, (255, 255, 255)), (const['width']//2-const['font_size'], const['height']//2-const['font_size']))
    board = fill2_4(board)
    board = fill2_4(board)
    return board

def restart(board,theme,text):
    board = newGame(theme,text)
    return board

def display(board,theme,text):
    screen.fill((0,0,0))
    for i in range(4):
        for j in range(4):
            pygame.draw.rect(screen, const[theme][str(board[i][j])], (const['margin']+(const['width']+const['margin'])*j//4, const['margin']+(const['height']+const['margin'])*i//4, const['width']//4-const['margin'], const['height']//4-const['margin']))
            if board[i][j] != 0:
                text = font.render(str(board[i][j]), True, (255, 255, 255))
                screen.blit(text, (const['margin']+(const['width']+const['margin'])*j//4+const['width']//8-const['font_size']//4, const['margin']+(const['height']+const['margin'])*i//4+const['height']//8-const['font_size']//4))
    pygame.display.flip()

def playgame(theme,dif):
    board = newGame(theme, "2048")
    display(board,theme,"2048")
    status = "KEEP PLAYING"
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    board = move_left(board)
                elif event.key == K_RIGHT:
                    board = move_right(board)
                elif event.key == K_UP:
                    board = move_up(board)
                elif event.key == K_DOWN:
                    board = move_down(board)
                elif event.key == K_r:
                    board = restart(board,theme,"2048")
                display(board,theme,"2048")
                status = WinCheck(board,status,theme,"2048")
                if status == "YOU LOST":
                    text = font.render("YOU LOST", True, (255, 255, 255))
                    screen.blit(text, (const['width']//2-const['font_size'], const['height']//2-const['font_size']))
                    pygame.display.flip()
                    time.sleep(2)
                    board = restart(board,theme,"2048")
                    display(board,theme,"2048")
                if status == "YOU WON":
                    board = restart(board,theme,"2048")
                    display(board,theme,"2048")
        time.sleep(dif)