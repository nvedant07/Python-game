import pygame
from random import randint
import math

class BaseClass(pygame.sprite.Sprite):

	allsprites=pygame.sprite.Group()
	def __init__(self , x , y , image_string):

		pygame.sprite.Sprite.__init__(self)
		BaseClass.allsprites.add(self)

		self.image=pygame.image.load(image_string)

		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y

	def destroy(self,ClassName):
		ClassName.List.remove(self)
		BaseClass.allsprites.remove(self)
		del self

class Mario(BaseClass):

	List=pygame.sprite.Group()
	going_right=True
	def __init__(self , x , y , image_string):

		BaseClass.__init__(self , x , y , image_string)
		Mario.List.add(self)
		self.velx,self.vely=0,5
		self.jumping,self.going_down=False,False
		
	def motion(self,width,height):
		predicted_position=self.rect.x+self.velx
		if predicted_position<0:
			self.velx=0
		elif predicted_position + self.rect.width>width:
			self.velx=0

		self.rect.x+=self.velx
		self.__jump(height)
	def __jump(self,height):
		
		max_height=100
		
		if self.jumping:
			if self.rect.y<max_height:
				self.going_down=True
			if self.going_down:
				self.rect.y += self.vely

				predicted_position=self.rect.y+self.vely
				if predicted_position+self.rect.height>height:
					self.going_down=False
					self.jumping=False
			else:
				self.rect.y-=self.vely

class Enemy(BaseClass):

	List=pygame.sprite.Group()
	def __init__(self , x , y , image_string):
		BaseClass.__init__(self , x , y , image_string)
		Enemy.List.add(self)
		self.health=100
		# self.half_health=self.health/2.0
		self.velx,self.vely=randint( 1 , 11),2
		self.amplitude,self.period=randint(600,640),randint(4,5)/100.0

	@staticmethod
	def update_all(width,height):
		for fly in Enemy.List:
			
			if fly.health<=0:
			 	#fly.destroy(Enemy)
			 	fly.velx=0
			 	if fly.rect.y+fly.rect.height<height:
			 		fly.rect.y+=fly.vely
			else:
				fly.fly(width,height)
	
	def fly(self,width,height):
		if self.rect.x + self.velx > width or self.rect.x<0:
			self.image = pygame.transform.flip(self.image,True,False)
			self.velx = -self.velx
		self.rect.x += self.velx
		self.rect.y = self.amplitude * math.sin(self.period * self.rect.x) 
		if self.rect.y<0:
			# self.image = pygame.transform.flip(self.image,False,True)
			self.rect.y=0

	# @staticmethod
	# def movement(width,height):
	# 	for fly in Enemy.List:
	# 		fly.fly(width,height)

class BugProjectile(BaseClass):
	List=pygame.sprite.Group()
	normal_list=[]
	fire=True
	def __init__(self , x , y ,bool_fire, image_string):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load(image_string)

		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.bool_fire=bool_fire

		try:
			last_projectile=BugProjectile.normal_list[-1]
			difference=abs(self.rect.x - last_projectile.rect.x)

			if difference<self.rect.width:
				return

		except Exception:
			pass


		BugProjectile.normal_list.append(self)
		BugProjectile.List.add(self)
		self.velx=None
	@staticmethod
	def movement():
		for projectile in BugProjectile.List:
			projectile.rect.x+=projectile.velx

	def destroy(self):
		BugProjectile.List.remove(self)
		BugProjectile.normal_list.remove(self)
		del self