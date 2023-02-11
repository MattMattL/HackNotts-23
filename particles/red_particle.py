# import the child classes
import random
import math

from particles.particle_handler import ParticleHandler
import numpy as np
import pygame

# extend your particle class with ParticleHandler
class RedParticle(ParticleHandler):

	def __init__(self):
		self.ID = "RED PARTICLE"
		self.posY = random.randint(0, 1000)
		self.posX = random.randint(0, 1600)
		self.m = 20

	# override all the initialisers:
	def start(self):
		""" Called once when the game starts """
		pass

	def isAffectedBy(self, particleID):
		if particleID in ["RED PARTICLE", "GREEN PARTICLE", "YELLOW PARTICLE"] : return True

		return False

	def F(self, x, y):
		rx, ry = -x + self.posX, -y + self.posY
		rn = (rx*rx + ry*ry)

		if rn <= 5: # repel
			return (0, 0) if rn == 0 else ((1 / rn**3)*rx, (1 / rn**3)*ry)
		elif rn <= 10: # attract
			return (0, 0) if rn == 0 else ((-1 / rn**3)*rx, (-1 / rn**3)*ry)
		else:
			return ((1 / rn**3)*rx, (1 / rn**3)*ry)

	def draw(self, window):
		return pygame.draw.circle(window, color=(255, 0, 0), center=(self.posX, self.posY), radius=2)

	def postUpdate(self):
		""" Called at the end of each frame """
		pass