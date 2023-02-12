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
		Fx = 1000*(self.posY - 300)
		Fy = 1000*(-self.posX + 500)
		return Fx,Fy

	def postUpdate(self):
		pass
