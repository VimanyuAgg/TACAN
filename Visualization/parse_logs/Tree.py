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

  # end func


  def add_node(self, node, parent=None):
    """

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
