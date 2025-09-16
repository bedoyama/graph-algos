from typing import Union
from .edge import Edge

class Node:
    def __init__(self, index: int, label=None):
        self.index: int = index
        self.edges: dict = {}
        self.label = label

    def num_edges(self) -> int:
        return len(self.edges)
    
    def get_edge(self, neighbor: int) -> Union[Edge,None]:
        if neighbor in self.edges:
            return self.edges[neighbor]
        return None

    def add_edge(self, neighbor: int, weight: float):
        edge = Edge(self.index, neighbor, weight)
        self.edges[neighbor] = edge

    def remove_edge(self, neighbor: int):
        if neighbor in self.edges:
            del self.edges[neighbor]

    def get_edge_list(self) -> list:
        return list(self.edges.values())
    
    def get_sorted_edge_list(self) -> list:
        result = []
        neighbors = (list)(self.edges.keys())
        neighbors.sort()

        for neighbor in neighbors:
            result.append(self.edges[neighbor])
        return result
    
    def get_neighbors(self) -> set:  
        neighbors: set = set()
        for edge in self.edges.values():
            neighbors.add(edge.to_node)
        return neighbors

    def get_out_neighbors(self) -> set:  
        neighbors: set = set()
        for edge in self.edges.values():
            neighbors.add(edge.to_node)
        return neighbors

