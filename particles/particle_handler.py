# handler class containing things to be used in parent classes

class ParticleHandler():

	def __init__(self):
		self.ID = None
		self.posY = None
		self.posX = None


	def start(self):
		pass

	def isAffectedBy(self, particleID):
		return False

	def baseField(self):
		Fx = self.posY - 600/2
		Fy = -self.posX + 1000/2
		return Fx,Fy

	def update(self, particles, dt):
		pass

	def postUpdate(self):
		pass
