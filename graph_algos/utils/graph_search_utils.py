from graph_algos.entities.graph import Graph
from graph_algos.entities.node import Node

class GraphSearchUtils:

    @staticmethod
    def dfs_recursive_basic(g:Graph, ind:int, seen:list):
        seen[ind]=True
        current: Node = g.nodes[ind]

        for edge in current.get_edge_list():
            if not seen[edge.to_node]:
                GraphSearchUtils.dfs_recursive_basic(g, edge.to_node, seen)

    @staticmethod
    def depth_first_search(g:Graph, start:int):
        seen: list = [False]*g.num_nodes
        GraphSearchUtils.dfs_recursive_basic(g, start, seen)

    @staticmethod
    def depth_first_search_basic_all(g: Graph): 
        seen: list = [False] * g.num_nodes
        for ind in range(g.num_nodes):
            if not seen[ind]:
                GraphSearchUtils.dfs_recursive_basic(g, ind, seen)

    @staticmethod
    def dfs_recursive_path(g: Graph, ind: int, seen: list, last: list): 
        seen[ind] = True
        current: Node = g.nodes[ind]

        for edge in current.get_edge_list():
            neighbor: int = edge.to_node
            if not seen[neighbor]:
                last[neighbor] = ind
                GraphSearchUtils.dfs_recursive_path(g, neighbor, seen, last)

    @staticmethod
    def depth_first_search_path(g: Graph) -> list: 
        seen: list = [False] * g.num_nodes
        last: list = [-1] * g.num_nodes

        for ind in range(g.num_nodes):
            if not seen[ind]:
                GraphSearchUtils.dfs_recursive_path(g, ind, seen, last)
        return last
