# handler class containing things to be used in parent classes

class ParticleHandler():

	def __init__(self):
		self.ID = None
		self.posY = None
		self.posX = None
		self.m = None


	def start(self):
		pass

	def isAffectedBy(self, particleID):
		return False

	def baseField(self):
		Fx = self.posY - 300
		Fy = -self.posX + 500
		return Fx,Fy

	def update(self, pGroups, dt):
		""" Called at the start of each frame. Update x and y here """
		dxB, dyB = self.baseField()
		self.posX += dxB / 10000
		self.posY += dyB / 10000

		for pType in pGroups:
			for particle in pType:
				deltaX, deltaY = particle.F(self.posX, self.posY)
				self.posX += particle.m*deltaX*dt
				self.posY += particle.m*deltaY*dt

	def postUpdate(self):
		pass
