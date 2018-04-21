def draw(list_of_nodes):
  """
  Will be invoked every time there is a change in the topology.

  list_of_nodes samples:
  1)
  [{'children': [{'children': [{'children': [{'children': [],
                                            'name': 'Node 9'}],
                              'name': 'Node 4'}],
                'name': 'Node 2'}],
  'name': 'Node 0'},
 {'children': [{'children': [], 'name': 'Node 10'}], 'name': 'Node 8'},
 {'children': [{'children': [], 'name': 'Node 6'}], 'name': 'Node 7'},
 {'children': [{'children': [], 'name': 'Node 3'},
               {'children': [{'children': [], 'name': 'Node 11'}],
                'name': 'Node 5'}],
  'name': 'Node 1'}]

  2)
  [{'children': [{'children': [], 'name': 'Node 1'}], 'name': 'Node 0'}]

  :param list_of_nodes: samples provided above
  :type list_of_nodes: [dict]
  :return: None
  Visualization/parse_logs/Draw.py
  """
  pass
  # raise NotImplementedError()
  # print list_of_nodes