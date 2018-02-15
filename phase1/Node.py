import weightMatrix

class Node:
	'''
	Node class representing each node in the network
	'''
	def __init__(self,myId,parentId, childListId,dist, clusterheadId,subtreeList,neighbourList,isClusterhead,state):
		self.id = myId
		self.parentId = parentId
		self.childListId = childListId
		self.dist = dist
		self.clusterheadId = clusterheadId
		self.subtreeList = subtreeList
		self.neighbourList = neighbourList
		self.weight = weightMatrix.getWeight(self.id)
		self.childWeightList = self.getChildWeight()
		self.isClusterhead = isClusterhead
		self.state = state

	def getChildWeight(self):
		childWeight = 0
		for c in self.childListId:
			childWeight += weightMatrix.getWeight(c)
		return childWeight

def testNode():
	n0 = Node
	n1 = Node(1,0,[4],1,0,[4],[2,3],False,"active")
	# print n1.parentId
	assert n1.parentId == 0
	print "Test 1 Passed"

	assert n1.weight == 176
	print "Test 2 Passed"

	assert n1.neighbourList == [2,3]
	print "Test 3 Passed - Integration with weightMatrix achieved"


testNode()


