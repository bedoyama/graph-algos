from graph_algos.entities.graph.graph import Graph
from graph_algos.entities.graph.node import Node


class TopologicalOrdering:
    @staticmethod
    def is_topo_ordered(g: Graph, ordering: list) -> bool: 
        if len(ordering) != g.num_nodes:
            return False

        index_to_pos: list = [-1] * g.num_nodes
        for pos in range(g.num_nodes):
            current: int = ordering[pos]
            if index_to_pos[current] != -1:
                return False
            index_to_pos[current] = pos

        for n in g.nodes:
            for edge in n.get_edge_list():
                if index_to_pos[edge.to_node] <= index_to_pos[n.index]:
                    return False
        return True
    
    # Khan's algorithm: https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm
    # L ← Empty list that will contain the sorted elements
    # S ← Set of all nodes with no incoming edge

    # while S is not empty do
    #     remove a node n from S
    #     add n to L
    #     for each node m with an edge e from n to m do
    #         remove edge e from the graph
    #         if m has no other incoming edges then
    #             insert m into S

    # if graph has edges then
    #     return error   (graph has at least one cycle)
    # else 
    #     return L   (a topologically sorted order)
    @staticmethod
    def Kahns(g: Graph) -> list: 
        count: list = [0] * g.num_nodes
        s: list = []
        result: list = []

        for current in g.nodes:
            for edge in current.get_edge_list():
                count[edge.to_node] = count[edge.to_node] + 1
        for current in g.nodes:
            if count[current.index] == 0:
                s.append(current.index)

        while len(s) > 0:
            current_index: int = s.pop()
            result.append(current_index)
            for edge in g.nodes[current_index].get_edge_list():
                count[edge.to_node] = count[edge.to_node] - 1
                if count[edge.to_node] == 0:
                    s.append(edge.to_node)
        return result

    @staticmethod
    def topological_dfs_recursive(g: Graph, index: int, seen: list, s: list):
        seen[index] = True
        current: Node = g.nodes[index]
        for edge in current.get_edge_list():
            neighbor: int = edge.to_node
            if not seen[neighbor]:
                TopologicalOrdering.topological_dfs_recursive(g, neighbor, seen, s)
        s.append(index)

    @staticmethod
    def topological_dfs(g: Graph) -> list: 
        seen: list = [False] * g.num_nodes
        s: list = []
        for ind in range(g.num_nodes):
            if not seen[ind]:
                TopologicalOrdering.topological_dfs_recursive(g, ind, seen, s)
        s.reverse()
        return s

    @staticmethod
    def check_cycle_kahns(g: Graph) -> bool:  
        result: list = TopologicalOrdering.Kahns(g)
        if len(result) == g.num_nodes:
            return False
        return True

    @staticmethod
    def sort_forward_pointers(options: list) -> list:
        num_nodes: int = len(options)
        g: Graph = Graph(num_nodes)
        for current in range(num_nodes):
            for next_index in options[current]:
                if next_index != -1:
                    g.insert_edge(current, next_index, 1.0)
        return TopologicalOrdering.Kahns(g)