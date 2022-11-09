from pygame import gfxdraw
import numpy as np
from math import cos, sin, sqrt, pow



def circulo_parametrico(window, color, posStart, posNow):
	
	x1,y1 = posStart
	x2,y2 = posNow
	radius = int(sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2)))
	pi = 3.14
	rangeValues = np.linspace(0, 2*pi, 1000)

	for a in rangeValues:
		x = radius * cos(a)
		y = radius * sin(a)
		gfxdraw.pixel(window, int(x1+x), int(y1+y), color)