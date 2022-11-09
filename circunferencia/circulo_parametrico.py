import pygame
from pygame import gfxdraw
import numpy as np
from math import cos, sin, sqrt, pow



def parametric_circle(window, color, posStart, posNow):
	from numpy import linspace
	
	x1,y1 = posStart
	x2,y2 = posNow
	radius = int(sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2)))
	pi = 3.14
	rangeValues = np.linspace(0, 2*pi, 1000)

	for a in rangeValues:
		x = radius * cos(a)
		y = radius * sin(a)
		gfxdraw.pixel(window, int(x1+x), int(y1+y), color)

	
window = pygame.display.set_mode((1200, 600))
points = []
begin = False

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			
	window.fill((255, 255, 255))

	if any(pygame.mouse.get_pressed()) and not begin:
		posStart = pygame.mouse.get_pos()
		begin = True

	if begin:
		posNow = pygame.mouse.get_pos()
		#circle(window, (255,0,0), posStart, posNow)
		parametric_circle(window, (255,0,0), posStart, posNow)

	if not any(pygame.mouse.get_pressed()) and begin:
		points.append((posStart, posNow))
		begin = False

	for i in range(len(points)):
		#circle(window, (0,0,0), points[i][0], points[i][1])
		parametric_circle(window, (0,0,0), points[i][0], points[i][1])
		
	pygame.display.flip()