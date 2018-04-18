class Tree(object):
  def __init__(self):
    self.data = []


  def _search_and_append(self, curr_node, to_append, parent):
    if 'name' in curr_node:
      if int(curr_node['name'][5:]) == parent:
        append_node = {
          'name': 'Node %d' % to_append,
          'children': []
        }
        curr_node['children'].append(append_node)
        return True

    for child in curr_node['children']:
      if self._search_and_append(curr_node=child, to_append=to_append, parent=parent):
        return True
    return False
  # end func


  def add_node(self, node, parent=None):
    """
    Append node to parent.

    :param node:
    :type node: int
    :param parent:
    :return:
    """
    node = int(node)
    if parent:
      parent = int(parent)

    if parent is None:
      child = {
        'name': 'Node %d' % node,
        'children': []
      }
      self.data.append(child)
      return True

    for n in self.data:
      if self._search_and_append(curr_node=n, to_append=node, parent=parent):
        return True

    print "parent not found"
    return False  # raise Error - parent not found
  # end func


  def _search_and_prune(self, curr_node, to_prune, parent):
    if 'name' in curr_node:
      if int(curr_node['name'][5:]) == to_prune:
        parent['children'].remove(curr_node)
        self.data.append(curr_node)
        return True

    for child in curr_node['children']:
      if self._search_and_prune(curr_node=child, to_prune=to_prune, parent=curr_node):
        return True
    return False
  # end func


  def prune(self, nodeid):
    nodeid = int(nodeid)
    node_name = 'Node %d' % nodeid
    for n in self.data:
      if self._search_and_prune(curr_node=n, to_prune=nodeid, parent=self.data):
        return True

    print "node not found"
    return False  # raise Error - node not found
  # end func

