import pygame
import random
import numpy as np
import math

# import the child classes
#from particles.particle_handler import ParticleHandler

# extend your particle class with ParticleHandler
class FairuzParticle: #(ParticleHandler):

	def __init__(self):
		self.ID = "FAIRUZ PARTICLE"
		self.posX = random.randint(100, 900)
		self.posY = random.randint(100, 500)
		#self.radius = 5

		self.window = pygame.display.set_mode((1600, 900))


		self.red = (255, 0, 0)
		self.green = (0, 255, 0)
		self.blue = (0, 0, 255)
		self.yellow = (255, 255, 0)
		self.cyan = (0, 255, 255)
		self.magenta = (255, 0, 255)

		self.colors_list = [self.red, self.green, self.blue, self.yellow, self.cyan, self.magenta]

		self.running = True
		self.clock = pygame.time.Clock()

	# override all the initialisers:
	def start(self):
		""" Called once when the game starts """
		pass

	def isAffectedBy(self, particleID):
		if particleID == "FAIRUZ PARTICLE":
			return True

		return False

#
	
	def createParticlesDict(self, color, x, y, radius, vx, vy):
		return {"color": color, "x": x, "y": y, "radius": radius, "vx": vx, "vy": vy}
	
	# updates particle dictionary above and returns a list of multiple particles
	def multipleParticles(self, numOfParticles, color, radius):
		particle_list = []
		for i in range(numOfParticles):
			#color = random.choice(self.colors_list)
			#x = random.randint(0, 1600)
			#y = random.randint(0, 900)
			vx = 0
			vy = 0
			if color == self.red:
				x = random.randint(100, 600)
				y = random.randint(50, 400)
			elif color == self.cyan:
				x = random.randint(800, 1500)
				y = random.randint(400, 800)
			particle_list.append(self.createParticlesDict(color, x, y, radius, vx, vy))
		return particle_list

	
	def drawParticle(self, color, x, y, radius):
		pygame.draw.circle(self.window, color, (x, y), radius)

	def createParticles(self, particles):
		for particle in particles:
			self.drawParticle(particle["color"], particle["x"], particle["y"], particle["radius"])

#	
	def interaction(self, particles1, particles2, particles3, G):
		for i in range(len(particles1)):
			fx = 0
			fy = 0

			for j in range(len(particles2)):
				pA = particles1[i]
				pB = particles2[j]
				dx = pA["x"] - pB["x"]
				dy = pA["y"] - pB["y"]
				r = math.sqrt(dx**2 + dy**2)

				if r > 0:
					F = G * 1/r
					fx += F*dx
					fy += F*dy
			
			pA["vx"] = (pA["vx"] + fx)/2
			pB["vy"] = (pA["vy"] + fy)/2

			pA["x"] += pA["vx"]
			pA["y"] += pA["vy"]

		for k in range(len(particles3)):
			pC = particles3[k]
			pC["x"] += pA["vx"]*2
			pC["y"] += pC["vy"]*2

			
		self.window.fill(0)

			


		

	def update(self):
		""" Called at the start of each frame. Update x and y here """
		"""
		for type in particles:
			for particle in type:
				# update x and y
				pass
		"""
		self.redParticles = self.multipleParticles(50, self.red, 5)

		self.cyanParticles = self.multipleParticles(100, self.cyan, 2)
		
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
			
			self.createParticles(self.redParticles)
			self.createParticles(self.cyanParticles)

			pygame.display.update()

			self.interaction(self.cyanParticles, self.cyanParticles, self.redParticles, -0.5)

		pygame.quit()

	def postUpdate(self):
		""" Called at the end of each frame """
		pass


def main():
	particleLife = FairuzParticle()
	particleLife.update()

if __name__ == "__main__":
    main()