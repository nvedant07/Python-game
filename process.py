import pygame,sys,classes,random

def process(mario,FPS,total_frames):
	for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_e:
					classes.BugProjectile.fire=not classes.BugProjectile.fire

	keys=pygame.key.get_pressed()
	if keys[pygame.K_d]:
		classes.Mario.going_right=True
		mario.image=pygame.image.load("images/mario.png")
		mario.velx=10
	elif keys[pygame.K_a]:
		classes.Mario.going_right=False
		mario.image=pygame.image.load("images/marioflipped.png")
		mario.velx= -10
	
	else:
		mario.velx=0
	
	if keys[pygame.K_w]:
		mario.jumping=True

	if keys[pygame.K_SPACE]:
		# p=classes.BugProjectile(mario.rect.x,mario.rect.y,21,25,"projectiles/fire.png")
		if classes.Mario.going_right:
			if classes.BugProjectile.fire:
				p=classes.BugProjectile(mario.rect.x+mario.rect.width,mario.rect.y,True,"projectiles/fire.png")
				p.velx=12
			else:
				p=classes.BugProjectile(mario.rect.x+mario.rect.width,mario.rect.y,False,"projectiles/ice.png")
				p.velx=12
		else:
			if classes.BugProjectile.fire:
				p=classes.BugProjectile(mario.rect.x,mario.rect.y,True,"projectiles/fire.png")
				p.image=pygame.transform.flip(p.image,True,False)
				p.velx=-12
			else:
				p=classes.BugProjectile(mario.rect.x,mario.rect.y,False,"projectiles/ice.png")
				p.image=pygame.transform.flip(p.image,True,False)
				p.velx=-12

	spawn(FPS,total_frames)
	collisions()

def spawn(FPS,total_frames):
	four_seconds=FPS*4

	if(total_frames%four_seconds==0):
		r=random.randint(1,2)
		x=1
		if r==2:
			x=1920-49
		classes.Enemy(x,500,"images/enemy.jpg")

def collisions():
	# pygame.sprite.groupcollide(G1,G2,dokill(g1),dokill(g2))
	for fly in classes.Enemy.List:

		# fly_proj=pygame.sprite.spritecollide(fly,classes.BugProjectile.List,True)
		# if len(fly_proj)>0:
		# 	for hit in fly_proj:
		# 		fly.health-=fly.half_health
		
	# 	if pygame.sprite.spritecollide(fly,classes.BugProjectile.List,False):
	# 		if classes.BugProjectile.fire:
	# 			fly.health-=fly.half_health
	# 		else:
	# 			fly.velx=0
	# for proj in classes.BugProjectile.List:

	# 	if pygame.sprite.spritecollide(proj,classes.Enemy.List,False):
	# 		proj.rect.x=2* -proj.rect.width
	# 		proj.destroy()
		

		projectiles=pygame.sprite.spritecollide(fly,classes.BugProjectile.List,True)
		for projectile in projectiles:
			
			fly.health=0
			if projectile.bool_fire:
				fly.image=pygame.image.load("images/burning_enemy.jpg")
			else:
				if fly.velx > 0:
					fly.image=pygame.image.load("images/frozen_enemy.png")
				else:
					fly.image=pygame.image.load("images/frozen_enemy.png")
					fly.image=pygame.transform.flip(fly.image,True,False)
			
			projectile.rect.x=2* -projectile.rect.width
			projectile.destroy()

