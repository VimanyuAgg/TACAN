_SPANNING_TREE_FILE_DIR = 'phase1/'
# _LOG_FILE = '../../phase1/logs/2018-04-16-info.log'
_LOG_FILE = '../../phase1/logs/2018-04-17-info.log'

# TODO: use relative imports
import sys, os
from os.path import dirname

project_home = dirname(dirname(sys.path[0]))
to_ins = os.path.join(project_home, _SPANNING_TREE_FILE_DIR)
# print to_ins
sys.path.insert(0, to_ins)

from spanning_tree import SPANNING_INFO
# print spanning_tree.SPANNING_INFO

from Tree import Tree
import pprint

pp= pprint.PrettyPrinter()

tree = Tree()

with open(_LOG_FILE, 'r') as fp:
  lines = fp.readlines()

for line in lines:
  if not line:
    continue
  last_part = line.split('-')[-1].strip()

  if last_part == 'Starting Server':
    print line
    node_id = line.split('-')[-2].split(':')[-1].strip()

    # print node_id
    if node_id in SPANNING_INFO:
      parent = SPANNING_INFO[node_id]['parentId']
    else:
      parent = None
    if parent:
      parent = int(parent)
    # print ('parent', parent)
    node_id = int(node_id)
    tree.add_node(node=node_id,parent=parent)
    # pp.pprint(tree.data)

  elif last_part == 'Got Prune':
    print line