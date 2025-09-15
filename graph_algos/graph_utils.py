from graph_algos.graph import Graph


class GraphUtils:
    @staticmethod
    def print_graph(graph: Graph):
        print(f"Graph with {graph.num_nodes} nodes, undirected={graph.undirected}")
        for node in graph.nodes:
            edge_list = node.get_edge_list()
            edges_str = ', '.join([f"({edge.source}->{edge.destination}, w={edge.weight})" for edge in edge_list])
            print(f"Node {node.index} [{node.label}]: {edges_str}")

    @staticmethod
    def clustering_coefficient(g: Graph, ind: int) -> float: 
        neighbors: set = g.nodes[ind].get_neighbors()
        num_neighbors: int = len(neighbors)

        count: int = 0
        for n1 in neighbors:
            for edge in g.nodes[n1].get_edge_list():
                if edge.to_node > n1 and edge.to_node in neighbors:
                    count += 1

        total_possible = (num_neighbors * (num_neighbors - 1)) / 2.0
        if total_possible == 0.0:
            return 0.0
        return count / total_possible
    
    @staticmethod
    def ave_clustering_coefficient(g: Graph) -> float:
        total: float = 0.0
        for n in range(g.num_nodes):
            total += GraphUtils.clustering_coefficient(g, n)

        if g.num_nodes == 0:
            return 0.0
        return total / g.num_nodes
    
    @staticmethod
    def check_node_path_valid(g: Graph, path: list) -> bool: 
        num_nodes_on_path: int = len(path)
        if num_nodes_on_path == 0:
            return True
        prev_node: int = path[0]
        if prev_node < 0 or prev_node >= g.num_nodes:
            return False

        for step in range(1, num_nodes_on_path):
            next_node: int = path[step]
            if not g.is_edge(prev_node, next_node):
                return False
            prev_node = next_node
        return True

    @staticmethod
    def check_edge_path_valid(g: Graph, path: list) -> bool: 
        if len(path) == 0:
            return True

        prev_node: int = path[0].from_node
        if prev_node < 0 or prev_node >= g.num_nodes:
            return False

        for edge in path:
            if edge.from_node != prev_node:
                return False

            next_node: int = edge.to_node
            if not g.is_edge(prev_node, next_node):
                return False

            prev_node = next_node
        return True
