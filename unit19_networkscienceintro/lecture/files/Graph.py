from collections import Counter
from pprint import pprint

import numpy as np
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, directed=False):
        self._nodes = {}
        self._edges = {}
        self._directed = directed


def add_method(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator


@add_method(Graph)
def add_node(self, node, **kwargs):
    self._nodes[node] = kwargs


@add_method(Graph)
def add_nodes_from(self, nodes, **kwargs):
    for node in nodes:
        if isinstance(node, tuple):
            self._nodes[node[0]] = node[1:]
        else:
            self._nodes[node] = kwargs


@add_method(Graph)
def add_edge(self, node_i, node_j, **kwargs):
    if node_i not in self._nodes:
        self.add_node(node_i)
    
    if node_j not in self._nodes:
        self.add_node(node_j)
    
    if node_i not in self._edges:
        self._edges[node_i] = {}
        
    if node_j not in self._edges[node_i]:
        self._edges[node_i][node_j] = {}
        
    self._edges[node_i][node_j] = kwargs
    
    if not self._directed:
        if node_j not in self._edges:
            self._edges[node_j] = {}

        if node_i not in self._edges[node_j]:
            self._edges[node_j][node_i] = {}

        self._edges[node_j][node_i] = kwargs
        
@add_method(Graph)
def add_edges_from(self, edges, **kwargs):
    for edge in edges:
        self.add_edge(*edge, **kwargs)


@add_method(Graph)
def edgelist(self):
    e = []
    
    for node_i in self._edges:
        for node_j in self._edges[node_i]:
            e.append([node_i, node_j, self._edges[node_i][node_j]])
            
    return e


@add_method(Graph)
def number_of_nodes(self):
    return len(self._nodes)


@add_method(Graph)
def degrees(self):
    deg = {}
    
    for node in self._nodes:
        if node in self._edges:
            deg[node] =  len(self._edges[node])
        else:
            deg[node] = 0
    
    return deg


@add_method(Graph)
def number_of_edges(self):
    n_edges = 0
    
    for node_i in self._edges:
        n_edges += len(self._edges[node_i])
    
    # If the graph is undirected, don't double count the edges
    if not self._directed:
        n_edges /= 2
    
    return n_edges


@add_method(Graph)
def is_directed(self):
    return self._directed


@add_method(Graph)
def weights(self, weight="weight"):
    w = {}
    
    for node_i in self._edges:
        for node_j in self._edges[node_i]:
            if weight in self._edges[node_i][node_j]:
                w[(node_i, node_j)] = self._edges[node_i][node_j][weight]
            else:
                w[(node_i, node_j)] = 1
    return w


@add_method(Graph)
def neighbours(self, node):
    return list(self._edges[node].keys())


@add_method(Graph)
def _build_distribution(data, normalize=True):
    values = data.values()
    dist = list(Counter(values).items())
    dist.sort(key=lambda x:x[0])
    dist = np.array(dist, dtype='float')
           
    if normalize:
        norm = dist.T[1].sum()
        dist.T[1] /= norm
    
    return dist


@add_method(Graph)
def degree_distribution(self, normalize=True):
    deg = self.degrees()
    dist = Graph._build_distribution(deg, normalize)
    
    return dist


@add_method(Graph)
def weight_distribution(self, normalize=True):
    deg = self.weights()
    dist = Graph._build_distribution(deg, normalize)
    
    return dist



@add_method(Graph)
def neighbour_degree(self):
    knn = {}
    deg = self.degrees()
    
    for node_i in self._edges:
        NN = self.neighbours(node_i)
        total = [deg[node_j] for node_j in NN]
        knn[node_i] = np.mean(total)
        
    return knn


@add_method(Graph)
def neighbour_degree_function(self):
    knn = {}
    count = {}
    deg = self.degrees()
    
    for node_i in self._edges:
        NN = self.neighbours(node_i)
        total = [deg[node_j] for node_j in NN]
        
        curr_k = deg[node_i]
        knn[curr_k] = knn.get(curr_k, 0) + np.mean(total)
        count[curr_k] = count.get(curr_k, 0) + 1
        
    for curr_k in knn:
        knn[curr_k]/=count[curr_k]
    
    knn = list(knn.items())
    knn.sort(key=lambda x:x[0])
    
    return np.array(knn)


