import math
import random
import pygame

from particles.particle_handler import ParticleHandler

class YellowParticle(ParticleHandler):

	def __init__(self):
		self.ID = "YELLOW PARTICLE"
		self.posX = random.randint(0, 1000)
		self.posY = random.randint(0, 500)
		self.m = 300

	# override all the initialisers:
	def start(self):
		""" Called once when the game starts """
		pass

	def isAffectedBy(self, particleID):
		if particleID in ["RED PARTICLE", "GREEN PARTICLE"] : return True

		return False

	def F(self, x, y):
		rx, ry = x - self.posX, y - self.posY
		rn = (rx*rx + ry*ry)**0.5

		return (0, 0) if rn == 0 else ((1 / rn**3)*rx, (1 / rn**3)*ry)

	def draw(self, window):
		return pygame.draw.circle(window, color=(255, 255, 0), center=(self.posX, self.posY), radius=3)


	def postUpdate(self):
		""" Called at the end of each frame """
		pass