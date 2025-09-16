from graph_algos.entities.graph import Graph


class GraphBuildUtils:
    @staticmethod
    def make_grid_graph(width: int, height: int) -> Graph: 
        num_nodes: int = width * height

        g: Graph = Graph(num_nodes, undirected=True)
        for r in range(height):
            for c in range(width):
                index: int = r * width + c

                if (c < width - 1):
                    g.insert_edge(index, index + 1, 1.0)
                if (r < height - 1):
                    g.insert_edge(index, index + width, 1.0)
        return g

    @staticmethod
    def make_grid_with_obstacles(width: int, height: int, obstacles: set) -> Graph: 
        num_nodes: int = width * height

        g: Graph = Graph(num_nodes, undirected=True)
        for r in range(height):
            for c in range(width):
                if (r, c) not in obstacles:
                    index: int = r * width + c
                if (c < width - 1) and (r, c + 1) not in obstacles:
                    g.insert_edge(index, index + 1, 1.0)
                if (r < height - 1) and (r + 1, c) not in obstacles:
                    g.insert_edge(index, index + width, 1.0)
        return g
