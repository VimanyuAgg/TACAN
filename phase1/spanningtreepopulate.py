from pymongo import MongoClient
import datetime, requests
from time import sleep

con = MongoClient('mongodb://localhost:27017/')
db = con.spanningtreemap

def populateTree():
	print "Inserting spanning tree into mongoDB...."
	db.spanningtree.insert([{
						'nodeId':'0',
						'parentId':None,
						'childListId':['1','2'],
						'dist':None,
						'clusterheadId':None,
						'subtreeList':[1,2,3,4,5,6],
						'neighbourList':None,
						'weight':None,
						'childWeightList':None,
						'isClusterhead':None,
						'state':"active",
						'rackLocation':'0,0'
					},
					 {	'nodeId':'1',
						'parentId':'0',
						'childListId':['3','5'],
						'dist':None,
						'clusterheadId':None,
						'subtreeList':['3','5'],
						'neighbourList':None,
						'weight':None,
						'childWeightList':None,
						'isClusterhead':None,
						'state':"active",
						'rackLocation':'0,1'
					},
					 {	'nodeId':'2',
						'parentId':'0',
						'childListId':['4','7'],
						'dist':None,
						'clusterheadId':None,
						'subtreeList':[1,2,3,4,5,6],
						'neighbourList':None,
						'weight':None,
						'childWeightList':None,
						'isClusterhead':None,
						'state':"active",
						'rackLocation':'0,2'
					},
						{'nodeId':'3',
						'parentId':'1',
						'childListId':None,
						'dist':None,
						'clusterheadId':None,
						'subtreeList':None,
						'neighbourList':None,
						'weight':None,
						'childWeightList':None,
						'isClusterhead':None,
						'state':"active",
						'rackLocation':'1,0'
					},
						{'nodeId':'4',
						'parentId':'2',
						'childListId':['9'],
						'dist':None,
						'clusterheadId':None,
						'subtreeList':None,
						'neighbourList':None,
						'weight':None,
						'childWeightList':None,
						'isClusterhead':None,
						'state':"active",
						'rackLocation':'1,1'
					},
					 {'nodeId':'5',
						 'parentId':'1',
						'childListId':['11'],
						'dist':None,
						'clusterheadId':None,
						'subtreeList':None,
						'neighbourList':None,
						'weight':None,
						'childWeightList':None,
						'isClusterhead':None,
						'state':"active",
						'rackLocation':'1,2'
					},
					{	'nodeId':'6',
						'parentId':'7',
						'childListId':None,
						'dist':None,
						'clusterheadId':None,
						'subtreeList':None,
						'neighbourList':None,
						'weight':None,
						'childWeightList':None,
						'isClusterhead':None,
						'state':"active",
						'rackLocation':'2,0'
					},
					{	'nodeId':'7',
						'parentId':'2',
						'childListId':['8'],
						'dist':None,
						'clusterheadId':None,
						'subtreeList':None,
						'neighbourList':None,
						'weight':None,
						'childWeightList':None,
						'isClusterhead':None,
						'state':"active",
						'rackLocation':'2,1'
					},
					{	'nodeId':'8',
						'parentId': '7',
						 'childListId': ['10'],
						 'dist': None,
						 'clusterheadId': None,
						 'subtreeList': None,
						 'neighbourList': None,
						 'weight': None,
						 'childWeightList': None,
						 'isClusterhead': None,
						 'state': "active",
						 'rackLocation': '2,2'
						 },
	{	'nodeId':'8',
						'parentId': '7',
						 'childListId': ['10'],
						 'dist': None,
						 'clusterheadId': None,
						 'subtreeList': None,
						 'neighbourList': None,
						 'weight': None,
						 'childWeightList': None,
						 'isClusterhead': None,
						 'state': "active",
						 'rackLocation': '2,2'
						 },
						{'nodeId':'9',
						'parentId': '4',
						 'childListId':None,
						 'dist': None,
						 'clusterheadId': None,
						 'subtreeList': None,
						 'neighbourList': None,
						 'weight': None,
						 'childWeightList': None,
						 'isClusterhead': None,
						 'state': "active",
						 'rackLocation': '0,3'
						 },
						{'nodeId':'10',
						'parentId': '8',
						 'childListId':None,
						 'dist': None,
						 'clusterheadId': None,
						 'subtreeList': None,
						 'neighbourList': None,
						 'weight': None,
						 'childWeightList': None,
						 'isClusterhead': None,
						 'state': "active",
						 'rackLocation': '1,3'
						 },
						{'nodeId':'11',
						'parentId': '5',
						 'childListId': None,
						 'dist': None,
						 'clusterheadId': None,
						 'subtreeList': None,
						 'neighbourList': None,
						 'weight': None,
						 'childWeightList': None,
						 'isClusterhead': None,
						 'state': "active",
						 'rackLocation': '2,3'
						 },
					 ])
	print "Done"