import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
speed = [2,2]
black = 0,0,0
width = 800
height = 600
gamer = pygame.image.load('mario.png')
ballrect = gamer.get_rect()
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]
	screen.fill(black)
	screen.blit(gamer, ballrect)
	pygame.display.flip()
