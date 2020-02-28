class Node:
	
	def __init__(self, data, nextP = None):
		self.data = data
		self.nextP = nextP

	#Getter Methods
	def getData(self):
		return self.data

	def getNextPointer(self):
		return self.nextP

	#Setter Methods
	def setData(self, newD):
		self.data = newD

	def setNextPointer(self, newP):
		self.nextP = newP

