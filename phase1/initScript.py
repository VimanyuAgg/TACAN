from Node import Node
from threading import Thread
import time

def spawnNode(id):
	return Node(id)

if __name__ == '__main__':
	thread0 = Thread(target=spawnNode, args=('0',))
	thread1 = Thread(target=spawnNode,args=('1',))
	thread2 = Thread(target=spawnNode, args=('2',))
	thread3 = Thread(target=spawnNode, args=('3',))
	thread4 = Thread(target=spawnNode, args=('4',))
	thread5 = Thread(target=spawnNode, args=('5',))
	thread6 = Thread(target=spawnNode, args=('7',))
	thread7 = Thread(target=spawnNode, args=('6',))
	thread8 = Thread(target=spawnNode, args=('8',))
	thread0.start()
	time.sleep(1)
	thread1.start()
	time.sleep(1)
	thread2.start()
	time.sleep(1)
	thread3.start()
	time.sleep(1)
	thread4.start()
	time.sleep(1)
	thread5.start()
	time.sleep(1)
	thread6.start()
	time.sleep(1)
	thread7.start()
	time.sleep(1)
	thread8.start()



