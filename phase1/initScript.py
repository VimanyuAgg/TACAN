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
	thread9 = Thread(target=spawnNode, args=('9',))
	thread10 = Thread(target=spawnNode, args=('10',))
	thread11 = Thread(target=spawnNode, args=('11',))
	thread0.start()
	time.sleep(2)
	thread1.start()
	time.sleep(2)
	thread2.start()
	time.sleep(2)
	thread3.start()
	time.sleep(2)
	thread4.start()
	time.sleep(2)
	thread5.start()
	time.sleep(2)
	thread6.start()
	time.sleep(2)
	thread7.start()
	time.sleep(2)
	thread8.start()
	time.sleep(2)
	thread9.start()
	time.sleep(2)
	thread10.start()
	time.sleep(2)
	thread11.start()



