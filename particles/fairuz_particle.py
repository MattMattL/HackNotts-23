import pygame
import random

# import the child classes
from particles.particle_handler import ParticleHandler

# extend your particle class with ParticleHandler
class FairuzParticle(ParticleHandler):

	def __init__(self):
		self.ID = "FAIRUZ PARTICLE"
		self.posX = random.randint(100, 900)
		self.posY = random.randint(100, 500)
		self.radius = 5

		self.red = (255, 0, 0)
		self.green = (0, 255, 0)
		self.blue = (0, 0, 255)
		self.yellow = (255, 255, 0)
		self.cyan = (0, 255, 255)
		self.magenta = (255, 0, 255)

		self.colors_list = [self.red, self.green, self.blue, self.yellow, self.cyan, self.magenta]

		self.clock = pygame.time.Clock()

	# override all the initialisers:
	def start(self):
		""" Called once when the game starts """
		pass

	def isAffectedBy(self, particleID):
		if particleID == "FAIRUZ PARTICLE":
			return True

		return False

	def update(self, particles):
		""" Called at the start of each frame. Update x and y here """
		for type in particles:
			for particle in type:
				# update x and y
				pass

	def postUpdate(self):
		""" Called at the end of each frame """
		pass

	def createParticlesDict(self, x, y, color):
		return {"x": x, "y": y, "color": color}
	
	def updateParticlesDict(self, numOfParticles):
		particle_list = []
		for i in range(numOfParticles):
			x = random.randint(1, self.radius/2 + 1)
			y = random.randint(1, self.radius/2 + 1)
			color = random.choice(self.colors_list)
			particle_list.append(self.createParticlesDict(x, y, color))