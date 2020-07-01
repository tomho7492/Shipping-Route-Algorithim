#Tommy Ho
#001329065

import csv
from trucks import Package, Truck
from interface import interface, completedTotalMilesInterface
from data import Graph, Vertex, ChainingHashTable
from datetime import time, timedelta
import datetime
from algorithim import algo2
from input import readPackages, readLocations

truck1 = Truck()
truck2 = Truck()
hashTable = ChainingHashTable()


milesList = [0]

readPackages('packages.csv', hashTable)

#construct a graph object
graph = Graph()

readLocations(graph)

#list of predefined truck package ids.
truck1LoadList = [14, 15,16,34,20,29,1,40,31,13,37,30]
truck2LoadList = [21, 28, 2, 10,38,3,8,32,6,36,12,18,23,25]
truck1LoadList2 = [19,4,33,7,5,9,39,27,35,17,24,26,22,11]

#truck 1's first load
#O(N)
for packageID in truck1LoadList:

    truck1.loadPackage(hashTable.search(packageID))
#O(N)
#truck 2's first load
for packageID in truck2LoadList:
    truck2.loadPackage(hashTable.search(packageID))


#O(N)
#get the hub vector
hub = []
for location in graph.adjacency_list:
    hub.append(location)
    break;

hub = hub[0]

#run the algorithims on truck1 and truck2 and their loads.
algo2(graph, hashTable, hub, truck1, milesList)
algo2(graph, hashTable, hub, truck2, milesList)
#O(N)
#truck 3's first load
for packageID in truck1LoadList2:
    truck1.loadPackage(hashTable.search(packageID))
#run the algo on truck3's load
algo2(graph, hashTable, hub, truck1, milesList)



completedTotalMilesInterface(milesList)

#this function takes user input to decide what to display. If 2 is pressed, it ask for package ID and a time and show you the package information at that point in time.
#if 3 is pressed, it will ask you for a time and display all packages at that point in time
interface(hashTable)
