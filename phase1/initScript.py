from Node import Node
from threading import Thread
import time

def spawnNode(id):
	return Node(id)

if __name__ == '__main__':
	threadPool= []
	for i in range(0,51):
		thread = Thread(target=spawnNode, args=(str(i),))
		threadPool.append(thread)

	for thread in threadPool:
		thread.start()
		time.sleep(2)



