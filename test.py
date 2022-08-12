import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame import Vector2 as Vec
from main import *

pygame.init()
win = pygame.display.set_mode((500, 500))

print(expansion("1-t", "t", 3, 1))

def drawCurve(win, points, color = (255, 255, 255)):
    for x in range(0, len(points)-1):
        pygame.draw.line(win, color, points[x], points[x+1])

b = bezier(3, [(0, 0), (75, 100), (200, 100), (250, 200)])

while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
    
    win.fill((0, 0, 0))
    drawCurve(win, b)
    pygame.display.update()