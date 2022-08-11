import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame import Vector2 as Vec

def expansion(exp1, exp2, deg, mode):
    pascal = str(11**deg)
    eq = ""
    for x in range(0, deg+1):
        eq += f"{pascal[x]}*({exp1})**{deg-x}*({exp2})**{x}"
        if x < deg:
            eq += " + "
    return eq if not mode else eq.split("+")

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
