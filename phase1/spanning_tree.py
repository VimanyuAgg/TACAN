"""
Later:
- everything string
- clusterhead IDs maintained for all subtree. as 'c0', 'c1'
- subtreeList not maintained
"""

SPANNING_INFO = {0: {'parentId': None,
                     'childListId': [1, 2],
                     'dist': None,
                     'clusterheadId': None,
                     'subtreeList': [1, 2, 3, 4, 5, 6],
                     'neighbourList': None,
                     'weight': None,
                     'childWeightList': None,
                     'isClusterhead': None,  # 1 or 0
                     'state': "active"
                     },
                 1: {'parentId': 0,
                     'childListId': [3, 5],
                     'dist': None,
                     'clusterheadId': 0,
                     'subtreeList': [3, 5],
                     'neighbourList': None,
                     'weight': None,
                     'childWeightList': None,
                     'isClusterhead': None,
                     'state': "active"
                     },
                 2: {'parentId': 0,
                     'childListId': [4, 6],
                     'dist': None,
                     'clusterheadId': 0,
                     'subtreeList': [1, 2, 3, 4, 5, 6],
                     'neighbourList': None,
                     'weight': None,
                     'childWeightList': None,
                     'isClusterhead': None,
                     'state': "active"
                     },
                 3: {'parentId': 1,
                     'childListId': None,
                     'dist': None,
                     'clusterheadId': 0,
                     'subtreeList': None,
                     'neighbourList': None,
                     'weight': None,
                     'childWeightList': None,
                     'isClusterhead': None,
                     'state': "active"
                     },
                 4: {'parentId': 2,
                     'childListId': None,
                     'dist': None,
                     'clusterheadId': 0,
                     'subtreeList': None,
                     'neighbourList': None,
                     'weight': None,
                     'childWeightList': None,
                     'isClusterhead': None,
                     'state': "active"
                     },
                 5: {'parentId': 1,
                     'childListId': None,
                     'dist': None,
                     'clusterheadId': 0,
                     'subtreeList': None,
                     'neighbourList': None,
                     'weight': None,
                     'childWeightList': None,
                     'isClusterhead': None,
                     'state': "active"
                     },
                 6: {'parentId': 2,
                     'childListId': None,
                     'dist': None,
                     'clusterheadId': 0,
                     'subtreeList': None,
                     'neighbourList': None,
                     'weight': None,
                     'childWeightList': None,
                     'isClusterhead': None,
                     'state': "active"
                     }}
