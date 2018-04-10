from pymongo import MongoClient
import datetime, requests
from time import sleep

con = MongoClient('mongodb://localhost:27017/')
db = con.spanningtreemap

db.spanningtree.insert([{'0':{'parentId':None,
					'childListId':[1,2],
					'dist':None,
					'clusterheadId':None,
					'subtreeList':[1,2,3,4,5,6],
					'neighbourList':None,
					'weight':None,
					'childWeightList':None,
					'isClusterhead':None,
					'state':"active",
					'rackLocation':'00'
				},
				 '1':{'parentId':0,
					'childListId':[3,5],
					'dist':None,
					'clusterheadId':None,
					'subtreeList':[3,5],
					'neighbourList':None,
					'weight':None,
					'childWeightList':None,
					'isClusterhead':None,
					'state':"active",
					'rackLocation':'01'
				},
				 '2':{'parentId':0,
					'childListId':[4,6],
					'dist':None,
					'clusterheadId':None,
					'subtreeList':[1,2,3,4,5,6],
					'neighbourList':None,
					'weight':None,
					'childWeightList':None,
					'isClusterhead':None,
					'state':"active",
					'rackLocation':'02'
				},
				 '3':{'parentId':1,
					'childListId':None,
					'dist':None,
					'clusterheadId':None,
					'subtreeList':None,
					'neighbourList':None,
					'weight':None,
					'childWeightList':None,
					'isClusterhead':None,
					'state':"active",
					'rackLocation':'10'
				},
				 '4':{'parentId':2,
					'childListId':None,
					'dist':None,
					'clusterheadId':None,
					'subtreeList':None,
					'neighbourList':None,
					'weight':None,
					'childWeightList':None,
					'isClusterhead':None,
					'state':"active",
					'rackLocation':'11'
				},
				 '5':{'parentId':1,
					'childListId':None,
					'dist':None,
					'clusterheadId':None,
					'subtreeList':None,
					'neighbourList':None,
					'weight':None,
					'childWeightList':None,
					'isClusterhead':None,
					'state':"active",
					'rackLocation':'12'
				},
				'6':{'parentId':2,
					'childListId':None,
					'dist':None,
					'clusterheadId':None,
					'subtreeList':None,
					'neighbourList':None,
					'weight':None,
					'childWeightList':None,
					'isClusterhead':None,
					'state':"active",
					'rackLocation':'20'
				},
				'7':{'parentId':2,
					'childListId':None,
					'dist':None,
					'clusterheadId':None,
					'subtreeList':None,
					'neighbourList':None,
					'weight':None,
					'childWeightList':None,
					'isClusterhead':None,
					'state':"active",
					'rackLocation':'21'
				},
				'8': {'parentId': 2,
					 'childListId': None,
					 'dist': None,
					 'clusterheadId': None,
					 'subtreeList': None,
					 'neighbourList': None,
					 'weight': None,
					 'childWeightList': None,
					 'isClusterhead': None,
					 'state': "active",
					 'rackLocation': '22'
					 }
				 }])


print "Inserting spanning tree into mongoDB...."
sleep(0.3)
print "Done"