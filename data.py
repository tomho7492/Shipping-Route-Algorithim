# Adjacency list
import csv

#defines a vertex class that serves as a location object
class Vertex:
    def __init__(self, label, address, index):
        self.label = label
        self.address = address
        self.index = index

    def __str__(self):
        return f"Label: {self.label},  Address: {self.address}, Index: {self.index}"
    def __repr__(self):
        return self.__str__()

#defines a graph class with an adjacency list and edge weights to store distances between two vertexes/locations.
#functions allow you to add a vertex, and create a distance between two locations by using add_undirected_edge. g
class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        if to_vertex in self.adjacency_list[from_vertex]:
            return None
        self.adjacency_list[from_vertex].append(to_vertex)


    def add_undirected_edge(self, vertex_a, vertex_b, weight):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)


    def getWeight(self, vertex2, vertex):

        vertexIndex =  vertex.index
        vertex2Index = vertex2.index

        distances = open('distances.csv', 'r', encoding='utf-8-sig')
        distances_reader = csv.reader(distances)
        distances_list = []
        #O(N)
        for distance in distances_reader:
            distances_list.append((distance))
        try:
            return float(distances_list[vertex2Index][vertexIndex])
        except:
            pass

    def getDistance(self, vertex2, vertex1):
        return self.edge_weights[(vertex2, vertex1)]


#This hash table is used to store packages via direct hashing. This works because each package has a unique ID.
#The insert function directly accesses the bucket and appends item
#search function directly accesses bucket and returns the list


# HashTable class
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=40):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        #O(N)
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
    def insert(self, item, hashNum):
        # get the bucket list where this item will go.
        bucket = hashNum-1
        bucket_list = self.table[bucket]

        # insert the item to the end of the bucket list.
        bucket_list.append(item)

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, hashNum):
        # get the bucket list where this key would be.
        bucket = hashNum-1
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
      #  if key in bucket_list:
            # find the item's index and return the item that is in the bucket list.
       #     item_index = bucket_list.index(key)
        if bucket_list is not None:
            return bucket_list[0]
        else:
            # the key is not found.
            return None

    # Removes an item with matching key from the hash table.
    def remove(self, key, hashNum):
        # get the bucket list where this item will be removed from.
        bucket = hashNum
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        if key in bucket_list:
            bucket_list.remove(key)
     #o(n)
    #resize function that allows the hash map to be self adjusting
    def resize(self, added_capacity):
        for i in range(added_capacity):
                self.table.append([])
