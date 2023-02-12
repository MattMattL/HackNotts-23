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

	def baseField(self, x=None, y=None):
		Fx = 8*(-self.posX + 1000)
		Fy = 8*(-self.posY + 700)

		Fx += 7*(self.posY - 800)
		Fy += 7*(-self.posX + 500)
		return Fx,Fy

	def postUpdate(self):
		pass
