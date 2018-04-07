from Node import Node
from threading import Thread

def spawnNode(id):
	return Node(id)

if __name__ == '__main__':
	thread1 = Thread(target=spawnNode(),args=(1,))
	thread2 = Thread(target=spawnNode(), args=(2,))
	node2 = Node(2)


