from trucks import Package
import csv
from data import Vertex
from algorithim import algo2

#read from csv file and create a package object will all the data and insert it into the hashtable.
def readPackages(file, hashTable):
    with open(file, 'r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file)
        # O(N)
        for package in csv_reader:
            id = int(package[0])
            city = package[2]
            address = (package[1])
            zip = int(package[4])
            deadline = package[5]
            weightInKilos = int(package[6])
            package = Package(id, address, city, zip, weightInKilos, deadline)

            """
            packageDict = {"package ID number": package.packageID, "delivery address": package.address,
                           "delivery deadline": package.deadline, "delivery city": package.city,
                           "delivery zip code": package.zip, "package weight": package.weightInKilos,
                           "delivery status": package.deliveryStatus, "delivery time": package.deliveryTime}
                           """
            hashTable.insert(package, package.ID)

def readLocations(graph):
    # read the location and distances csv files
    locations = open('locations.csv', 'r', encoding='utf-8-sig')
    locations_reader = csv.reader(locations)
    distances = open('distances.csv', 'r', encoding='utf-8-sig')
    distances_reader = csv.reader(distances)

    # O(N)
    # for every location from the csv file, create a vertex/location object and add it to the graph
    for location in locations_reader:
        vertex = Vertex(location[1], location[2], int(location[0]))
        graph.add_vertex(vertex)

        # O(N^2)
        # take 2 locations from the adjacency list and get the weight between the two. then use it to create a undirected edge and add it to the graph.
    for startLocation in graph.adjacency_list:
        for otherLocation in graph.adjacency_list:
            weight = graph.getWeight(otherLocation, startLocation)

            if weight is None:
                continue

            graph.add_undirected_edge(otherLocation, startLocation, weight)
