import pygame
from pygame import gfxdraw
import time
import numpy as np
from math import cos, sin, sqrt, pow



def circulo_convencional(window, color, posStart, posNow):

	x1,y1 = posStart
	x2,y2 = posNow
	radius = int(sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2)))

	rangeValues = np.linspace(radius, -radius, 1000)
	
	for x in rangeValues:
		y = sqrt(radius**2 - x**2)
		gfxdraw.pixel(window, int(x1+x), int(y1+y), color)
		gfxdraw.pixel(window, int(x1+x), int(y1-y), color)

	#for x in range(-radius, radius, 1):
	#	y = int(sqrt(radius**2 - x**2))
	#	gfxdraw.pixel(window, x1+x, y1+y, color)
	#	gfxdraw.pixel(window, x1+x, y1-y, color)