# import the child classes
import random

import numpy
import pygame

from particles.particle_handler import ParticleHandler

# extend your particle class with ParticleHandler
class ExampleParticle(ParticleHandler):

	def __init__(self):
		self.ID = "EXAMPLE PARTICLE"
		self.posY = 250
		self.posX = 500

	# override all the initialisers:
	def start(self):
		""" Called once when the game starts """
		pass

	def isAffectedBy(self, particleID):
		if particleID == "EXAMPLE PARTICLE":
			return True

		return False

	def update(self, particles, dt):
		""" Called at the start of each frame. Update x and y here """
		for pType in particles:
			for particle in pType:
				# dx , dy = particle.F(self.posX,self.posY)
				self.posX += random.randint(-2, 2)
				self.posY += random.randint(-2, 2)
				pass

	def draw(self, window):
		return pygame.draw.circle(window, color=(255, 100, 200), center=(self.posX, self.posY), radius=5)

	def postUpdate(self):
		""" Called at the end of each frame """
		pass
