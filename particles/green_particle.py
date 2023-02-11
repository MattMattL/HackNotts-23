# import the child classes
import random
import math

import numpy as np
import pygame

from particles.particle_handler import ParticleHandler

# extend your particle class with ParticleHandler
class GreenParticle(ParticleHandler):

	def __init__(self):
		self.ID = "GREEN PARTICLE"
		self.posY = random.randint(0, 1600)
		self.posX = random.randint(0, 1000)
		self.m = 10

	# override all the initialisers:
	def start(self):
		""" Called once when the game starts """
		pass

	def isAffectedBy(self, particleID):
		if particleID in ["GREEN PARTICLE", "YELLOW PARTICLE"] : return True

		return False

	def F(self, x, y):
		rx, ry = x - self.posX, y - self.posY
		rn = (rx*rx + ry*ry)

		fx, fy = 20 * math.sin(rx)/(rn+1), 20 * math.sin(ry)/(rn+1)

		if rn <= 80: # repel
			return fx, fy
		elif rn <= 140: # attract
			return fx, fy
		else:
			return fx, fy

	def draw(self, window):
		pygame.draw.circle(window, color=(0, 255, 0), center=(self.posX, self.posY), radius=5)

	def postUpdate(self):
		""" Called at the end of each frame """
		pass
