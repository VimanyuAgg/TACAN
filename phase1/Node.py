class Node:
	'''
	Node class representing each node in the network
	'''
	def __init__(self,myId,parentid, childList,dist, clusterheadid,isClusterhead,state):
		self.id = myId
		self.parentId = parentId
		self.childListId = childListId
		self.dist = dist
		self.clusterheadId = clusterheadid
		self.subtreeList = subtreeList
		self.neighbourList = neighbourList
		self.weight = weightMatrix.getWeight(self.id)
		self.childWeightList = self.getChildWeight()
		self.isClusterhead = isClusterhead
		self.state = state

	def getChildWeight():
		childWeight = 0
		for c in childListId:
			childWeight += weightMatrix.getWeight(c)
		return childWeight