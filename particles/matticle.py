import math
import random
import pygame

from particles.particle_handler import ParticleHandler

class MattsParticle(ParticleHandler):

	def __init__(self):
		self.ID = "MATTS PARTICLE"
		self.posX = random.randint(0, 1000)
		self.posY = random.randint(0, 500)

	# override all the initialisers:
	def start(self):
		""" Called once when the game starts """
		pass

	def isAffectedBy(self, particleID):
		if particleID == "EXAMPLE PARTICLE": return True
		if particleID == "MATTS PARTICLE": return False

		return False

	def update(self, pGroups, dt):
		""" Called at the start of each frame. Update x and y here """
		for pType in pGroups:
			for particle in pType:

				if particle.ID == "EXAMPLE PARTICLE":
					deltaX, deltaY = particle.posX - self.posX, particle.posY - self.posY

					self.posX += 10/deltaX
					self.posY += 10/deltaY

	def draw(self, window):
		return pygame.draw.circle(window, color=(100, 255, 200), center=(self.posX, self.posY), radius=3)


	def postUpdate(self):
		""" Called at the end of each frame """
		pass