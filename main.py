import pygame
from pygame import Vector2 as Vec

pygame.init()
win = pygame.display.set_mode((500, 500))

def expansion(exp1, exp2, deg, mode):
    pascal = str(11**deg)
    eq = ""
    for x in range(0, deg+1):
        eq += f"{pascal[x]}*({exp1})**{deg-x}*({exp2})**{x}"
        if x < deg:
            eq += " + "
    return eq if not mode else eq.split("+")

print(expansion("1-t", "t", 3, 1))
    
def beziur(deg, points=[], precision=400):
    if len(points) < deg:
        raise "Not enough points to form beziur equation"

    p = [Vec(x) for x in points]
    final = []
    for t in range(0, precision):
        e = expansion(str(1-(t/precision)), str(t/precision), deg, 1)
        newP = Vec(0, 0)
        for x in e:
            newP += eval(x)*p[e.index(x)]
        final.append(newP)

    return final

def drawCurve(win, points, color = (255, 255, 255)):
    for x in range(0, len(points)-1):
        pygame.draw.line(win, color, points[x], points[x+1])

b2 = beziur(3, [(0, 0), (5, 66.6), (95, 66.6), (100, 0)])
b = beziur(7, [(0, 0), (5, 66.6), (95, 66.6), (100, 0), (99, 200), (500, 500), (200, 43), (0, 50)])
while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
    
    win.fill((0, 0, 0))
    drawCurve(win, b)
    pygame.display.update()
    