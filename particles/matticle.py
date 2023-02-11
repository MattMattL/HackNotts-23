import random
from particles.particle_handler import ParticleHandler

class MattsParticle(ParticleHandler):

	def __init__(self):
		self.ID = "MATTS PARTICLE"
		self.posX = random.randint(100, 900)
		self.posY = random.randint(100, 400)

	# override all the initialisers:
	def start(self):
		""" Called once when the game starts """
		pass

	def isAffectedBy(self, particleID):
		if particleID == "EXAMPLE PARTICLE": return False
		if particleID == "MATTS PARTICLE": return True

		return False

	def update(self, particles, dt):
		""" Called at the start of each frame. Update x and y here """
		for pType in particles:
			for particle in pType:

				if particle.ID == "MATTS PARTICLE":
					deltaX, deltaY = particle.posX - self.posX, particle.posY - self.posY

					if deltaX != 0:
						self.posX += 1/deltaX

					if deltaY != 0:
						self.posY += 1/deltaY


	def postUpdate(self):
		""" Called at the end of each frame """
		pass