# Implementation of a simple weighted digraph with a Node class
# Three classes: State class, Node class, and Graph class
# Adjacency list representation

from enum import Enum
from collections import OrderedDict


class State(Enum):
    unvisited = 1  # white
    visited = 2  # black
    visiting = 3  # gray


# For the Node class will take advantage of the OrderedDict object
# in case want to keep track of the order keys are added to the dictionary
# OrderedDict will be useful for implementing BFS and DFS
class Node:

    def __init__(self, node_id):
        self.node_id = node_id  # id of this node (its key)
        self.visit_state = State.unvisited
        self.adjacent = OrderedDict()  # key = neighbor node (Node obj), val = weight

    def add_neighbor(self, adj_node, weight=0):  # adj_node is a Node obj
        self.adjacent[adj_node] = weight

    # special method, print
    def __str__(self):
        return str(self.node_id)


# Graph G = (V,E) is represented here by a standard adjacency list
class Graph:

    def __init__(self):
        self.nodes = OrderedDict()  # key = node id (not Node obj), val = node (Node obj)

    def add_node(self, node_id):
        v = Node(node_id)  # instantiate Node object
        self.nodes[node_id] = v  # add Node object to graph so v \in V
        return v

    def add_edge(self, source_id, dest_id, weight=0):
        # First check if source & dest nodes \in V
        if source_id not in self.nodes:
            self.add_node(source_id)
        if dest_id not in self.nodes:
            self.add_node(dest_id)

        self.nodes[source_id].add_neighbor(self.nodes[dest_id], weight)
