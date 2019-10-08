# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 11:44:57 2018

@author: pstmr
"""

import matplotlib.pyplot as plt
import numpy as np
import time as t
from math import cos, sin, pi


rayon = 1
modulo = 200

def get_points(n1, n2):
    x1 = rayon * cos(2*pi*n1/modulo)
    y1 = rayon * sin(2*pi*n1/modulo)
    
    x2 = rayon * cos(2*pi*n2/modulo)
    y2 = rayon * sin(2*pi*n2/modulo)
    
    return (x1, x2), (y1, y2)
    
def table(n):
    points = []
    for i in range(modulo):
        n2 = (i * n) % modulo
        points.append(get_points(i, n2))
        
    return points
    
    
def draw_lines(points):
    for p in points:
        plt.plot(p[0], p[1], color="black")
    
def rotate(deb, fin, mod=modulo, pres=100, pause=0.005):
    global modulo
    modulo, mod = mod, modulo
    nombres = np.linspace(deb, fin, pres)

    for i in nombres:
        p = table(i)
        
        plt.gcf().clear()
        draw_lines(p)
        plt.title("table de {} modulo {}".format(round(i, 2), modulo))
        plt.legend()
        plt.draw()
        
        t.sleep(pause)
        plt.pause(pause)
        
    modulo = mod
        
def draw_circle(tab, mod):
    global modulo
    modulo, mod = mod, modulo
    
    t = table(tab)
    draw_lines(t)
    
    plt.title("table de {} modulo {}".format(round(tab, 2), modulo))
    plt.legend()
    
    modulo = mod
    
#rotate(150, 151, 200)
draw_circle(805, 1000)