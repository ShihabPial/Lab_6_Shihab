from myNode import Node

class LinkedList:
	def __init__(self, head = None, size = 0, tail = None):
		self.head = head
		self.size = size
		self.tail = tail

	#Getter Methods
	def getHead(self):
		return self.head

	def getSize(self):
		return self.size

	def getTail(self):
		return self.tail

	#Setter Methods
	def setHead(self, newH):
		self.head = newH

	def setSize(self, newS):
		self.size = newS

	def setTail(self, newT):
		self.tail = newT

	#Other Mothods
	def isEmpty(self):
		if(self.getSize() == 0):
			return True
		return False

	def addNode(self, nData):
		newNode = Node(nData)

		if(self.isEmpty()):
			self.setHead(newNode)

		else:
			temp_tail = self.getTail()
			self.getTail().setNextPointer(newNode)
		
		self.setTail(newNode)
		self.setSize(self.size + 1)

def main():

	ll = LinkedList()
	ll.addNode(1000)
	ll.addNode(2000)

	print(ll.getTail().getData())

if __name__ == '__main__':
	main()