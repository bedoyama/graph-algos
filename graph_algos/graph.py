from typing import Union
from .node import Node
from .edge import Edge

class Graph:
    def __init__(self, num_nodes: int, undirected: bool=False): 
        self.num_nodes: int = num_nodes
        self.undirected: bool = undirected
        self.nodes: list = [Node(j) for j in range(num_nodes)]
    
    def get_edge(self, from_node: int, to_node: int) -> Union[Edge, None]: 
        if from_node < 0 or from_node >= self.num_nodes:
            raise IndexError
        if to_node < 0 or to_node >= self.num_nodes:
            raise IndexError
        return self.nodes[from_node].get_edge(to_node)

    def is_edge(self, from_node: int, to_node: int) -> bool: 
        return self.get_edge(from_node, to_node) is not None

    def make_edge_list(self) -> list:
        all_edges: list = []
        for node in self.nodes:
            for edge in node.edges.values():
                all_edges.append(edge)
        return all_edges

    def insert_edge(self, from_node: int, to_node: int, weight: float): 
        if from_node < 0 or from_node >= self.num_nodes:
            raise IndexError
        if to_node < 0 or to_node >= self.num_nodes:
            raise IndexError

        self.nodes[from_node].add_edge(to_node, weight)
        if self.undirected:
            self.nodes[to_node].add_edge(from_node, weight)

    def remove_edge(self, from_node: int, to_node: int): 
        if from_node < 0 or from_node >= self.num_nodes:
            raise IndexError
        if to_node < 0 or to_node >= self.num_nodes:
            raise IndexError

        self.nodes[from_node].remove_edge(to_node)
        if self.undirected:
            self.nodes[to_node].remove_edge(from_node)

    def insert_node(self, label=None) -> Node: 
        new_node: Node = Node(self.num_nodes, label=label)
        self.nodes.append(new_node)
        self.num_nodes += 1
        return new_node
    
    def make_copy(self): 
        g2: Graph = Graph(self.num_nodes, undirected=self.undirected)
        for node in self.nodes:
            g2.nodes[node.index].label = node.label
            for edge in node.edges.values():
                g2.insert_edge(edge.from_node, edge.to_node, edge.weight)
        return g2

    def get_in_neighbors(self, target: int) -> set:  
        neighbors: set = set()
        for node in self.nodes:
            if target in node.edges:
                neighbors.add(node.index)
        return neighbors
    
    def make_undirected_neighborhood_subgraph(self, ind: int, closed: bool):  
        if not self.undirected:
            raise ValueError

        nodes_to_use: set = self.nodes[ind].get_neighbors()
        if closed:
            nodes_to_use.add(ind)

        index_map = {}
        for new_index, old_index in enumerate(nodes_to_use):
            index_map[old_index] = new_index

        g_new: Graph = Graph(len(nodes_to_use), undirected=True)
        
        for n in nodes_to_use:
            for edge in self.nodes[n].get_edge_list():
                if edge.to_node in nodes_to_use and edge.to_node > n:
                    ind1_new = index_map[n]
                    ind2_new = index_map[edge.to_node]
                    g_new.insert_edge(ind1_new, ind2_new, edge.weight)

        return g_new

    def __str__(self):
        lines = [f"Graph with {self.num_nodes} nodes, undirected={self.undirected}"]
        for node in self.nodes:
            edge_list = node.get_edge_list()
            edges_str = ', '.join([f"({edge.source}->{edge.destination}, w={edge.weight})" for edge in edge_list])
            lines.append(f"Node {node.index} [{node.label}]: {edges_str}")
        return '\n'.join(lines)
