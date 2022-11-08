import pygame
from pygame import gfxdraw
import time
import numpy as np
from math import cos, sin, sqrt, pow



def circle(window, color, posStart, posNow):

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
		circle(window, (255,0,0), posStart, posNow)
		#parametric_circle(window, (255,0,0), posStart, posNow)

	if not any(pygame.mouse.get_pressed()) and begin:
		points.append((posStart, posNow))
		begin = False

	for i in range(len(points)):
		circle(window, (0,0,0), points[i][0], points[i][1])
		#parametric_circle(window, (0,0,0), points[i][0], points[i][1])
		
	pygame.display.flip()