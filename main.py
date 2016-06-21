import pygame,sys
from classes import *
from process import process

pygame.init()

width,height=1920,900
screen=pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption("Welcome")
clock=pygame.time.Clock()
FPS=24
total_frames=0

bg=pygame.image.load("images/bg.jpg")
mario=Mario(0,height-128,"images/mario.png")

# img_mario=pygame.image.load("mario.png")

clr1=(22,122,211)
clr2=(40,44,166) #0-255
clr3=(34,55,245)
# i=0
while True:
	process(mario,FPS,total_frames)
	# i+=5
	# if(i>255):
	# 	i %=255

	# screen.fill((i,i,255))
	mario.motion(width,height)
	Enemy.update_all(width,height)
	BugProjectile.movement()
	total_frames+=1

	screen.blit(bg,(0,0))
	BaseClass.allsprites.draw(screen)
	BugProjectile.List.draw(screen)
	# pygame.draw.line(screen,clr2,(0,0),(1080,1080),10)
	# pygame.draw.rect(screen,clr3,(40,40,200,300),1)
	# pygame.draw.circle(screen,clr1,(600,900),20,1)
	
	# screen.blit(img_mario,(500,500))

	pygame.display.flip()
	clock.tick(FPS)