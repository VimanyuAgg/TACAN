import weightMatrix
from spanning_tree import SPANNING_INFO
import raspberryPi_id_list

class Node:
	'''
	Node class representing each node in the network
	'''
	def __init__(self,myId):
		
		self.id = myId
		#self.parentId = parentId
		#self.childListId = childListId
		my_info = SPANNING_INFO[myId]
		self.parentId = my_info['parentId']
		self.childListId = my_info['childListId']
		self.dist = my_info['dist']
		self.clusterheadId = my_info['clusterheadId']
		self.subtreeList = my_info['subtreeList']
		self.neighbourList = my_info['neighbourList']
		self.weight = weightMatrix.getWeight(self.id)
		self.childWeightList = self.getChildWeight()
		self.isClusterhead = my_info['isClusterhead']
		self.state = my_info['state']
		

	def getChildWeight(self):
		childWeight = 0
		for c in self.childListId:
			childWeight += weightMatrix.getWeight(c)
		return childWeight

	def startPhaseOneClustering():
		self.size = weight
		if len(childListId) == 0:
			sendSize()

	# Connects to Raspberry Pi and registers its IP address on the central lookup
	# Can merge getIP and registerOnPi
	def registerOnPi():
		pass

	# Connects to Raspberry Pi (Central Service) and gets its IP address
	# Can merge getIP and registerOnPi
	def getIP():
		pass

	def getIPfromId(Id):
		return raspberryPi_id_list.ID_IP_MAPPING[Id]







def testNode():
	n0 = Node
	n1 = Node(1)
	# print n1.parentId
	assert n1.parentId == 0
	print "Test 1 Passed"

	assert n1.weight == 176
	print "Test 2 Passed"


testNode()


