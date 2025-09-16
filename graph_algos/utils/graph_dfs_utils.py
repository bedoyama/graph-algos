from graph_algos.entities.graph import Graph
from graph_algos.entities.node import Node

class GraphDFSUtils:

    @staticmethod
    def dfs_recursive_basic(g:Graph, ind:int, seen:list):
        seen[ind]=True
        current: Node = g.nodes[ind]

        for edge in current.get_edge_list():
            if not seen[edge.to_node]:
                GraphDFSUtils.dfs_recursive_basic(g, edge.to_node, seen)

    @staticmethod
    def depth_first_search(g:Graph, start:int):
        seen: list = [False]*g.num_nodes
        GraphDFSUtils.dfs_recursive_basic(g, start, seen)

    @staticmethod
    def depth_first_search_basic_all(g: Graph): 
        seen: list = [False] * g.num_nodes
        for ind in range(g.num_nodes):
            if not seen[ind]:
                GraphDFSUtils.dfs_recursive_basic(g, ind, seen)

    @staticmethod
    def dfs_recursive_path(g: Graph, ind: int, seen: list, last: list): 
        seen[ind] = True
        current: Node = g.nodes[ind]

        for edge in current.get_edge_list():
            neighbor: int = edge.to_node
            if not seen[neighbor]:
                last[neighbor] = ind
                GraphDFSUtils.dfs_recursive_path(g, neighbor, seen, last)

    @staticmethod
    def depth_first_search_path(g: Graph) -> list: 
        seen: list = [False] * g.num_nodes
        last: list = [-1] * g.num_nodes

        for ind in range(g.num_nodes):
            if not seen[ind]:
                GraphDFSUtils.dfs_recursive_path(g, ind, seen, last)
        return last

    @staticmethod
    def depth_first_search_stack(g: Graph, start: int) -> list: 
        seen: list = [False] * g.num_nodes
        last: list = [-1] * g.num_nodes
        to_explore: list = []

        to_explore.append(start)
        while to_explore:
            ind = to_explore.pop()
            if not seen[ind]:
                current: Node = g.nodes[ind]
                seen[ind] = True

            all_edges: list = current.get_sorted_edge_list()
            all_edges.reverse()
            for edge in all_edges:
                neighbor: int = edge.to_node
                if not seen[neighbor]:
                    last[neighbor] = ind
                    to_explore.append(neighbor)
        return last

    @staticmethod
    def dfs_recursive_cc(g: Graph, ind: int, component: list, curr_comp: int):  
        component[ind] = curr_comp
        current: Node = g.nodes[ind]

        for edge in current.get_edge_list():
            neighbor: int = edge.to_node
            if component[neighbor] == -1:
                GraphDFSUtils.dfs_recursive_cc(g, neighbor, component, curr_comp)

    @staticmethod
    def dfs_connected_components(g: Graph) -> list:
        component: list = [-1] * g.num_nodes
        curr_comp: int = 0

        for ind in range(g.num_nodes):
            if component[ind] == -1:
                GraphDFSUtils.dfs_recursive_cc(g, ind, component, curr_comp)
                curr_comp += 1

        return component
