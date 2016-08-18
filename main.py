import pygame
pygame.init()
width = 1500
height = 1300
screen = pygame.display.set_mode((height,width))
speed = [2,2]
black = 0,0,0
gamer = pygame.image.load('./images/mario.png')
x = 10
y = 10
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == 274:
				print('up')
				y = y+50
			if event.key == 273:
				print('down')
				y = y-50
			if event.key == 275:
				print('right')
				print(x)				
				x = x+50
				if x>500:
					x=10
			if event.key == 276:
				print('left')
				print(x)
				x = x-50


	screen.fill(black)
	screen.blit(gamer, (x,y))
	pygame.display.flip()
