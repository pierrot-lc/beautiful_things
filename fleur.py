# -*- coding: utf-8 -*-
"""
Created on Thu May 10 00:31:36 2018

@author: pstmr
"""

import matplotlib.pyplot as plt
from math import pi, sqrt
import numpy as np

from time import sleep

nbr_or = (1 + sqrt(5))/2

def get_points(nbr, pas, ratio, r0):
    points = []
    for i in range(nbr):
        points.append(r0*np.exp(1j*2*pi*i*ratio))
        r0 += pas
        
    return points
    
def init_plot(size=8, lim=5):
    axes = plt.gca()
    axes.set_xlim(-lim, lim)
    axes.set_ylim(-lim, lim)
    fig, = plt.plot([],[], 'r.', markersize=size)
    return fig
    
def tracer_points(points, fig, time=0.0001):
    X, Y = getXY(points)
    fig.set_xdata(X)
    fig.set_ydata(Y)
    plt.draw()
    plt.pause(time)
    sleep(time)
    
def getXY(points):
    return [i.real for i in points], [i.imag for i in points]
    
def rotate(nbr=50, pas=0.1, longueur=5e3):
    fig = init_plot()
    ratios = np.linspace(0, 1, longueur)
    plt.legend()
    for i in ratios:
        plt.title("ratio : 1/{}".format(round(1/i, 2)))
        tracer_points(get_points(nbr, pas, i, 0), fig)

def trace(nbr=500, pas=0.01, ratio=1/nbr_or):
    fig = init_plot()
    tracer_points(get_points(nbr, pas, ratio, 0), fig)

if __name__ == "__main__":
    rotate()