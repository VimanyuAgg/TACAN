import Node

from threading import Thread
from time import sleep

nodes = range(6)

for i in nodes:
  t = Thread(target=Node.Node, args=(i,))
  t.start()
  sleep(0.1)
