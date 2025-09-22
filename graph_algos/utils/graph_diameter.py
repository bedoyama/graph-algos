import math
from typing import Union
from graph_algos.algos.floyd_warshall import FloydWarshall
from graph_algos.entities.graph.edge import Edge
from graph_algos.entities.graph.graph import Graph


class GraphDiameter:
    @staticmethod
    def compute(g: Graph) -> float: 
        last: list = FloydWarshall.compute(g)
        max_cost: float = -math.inf

        for i in range(g.num_nodes):
            for j in range(g.num_nodes):
                cost: float = 0.0
                current: int = j

                while current != i:
                    prev: int = last[i][current]
                    if prev == -1:
                        return math.inf

                    edge: Union[Edge, None] = g.get_edge(prev, current)
                    cost = cost + edge.weight
                    current = prev

                if cost > max_cost:
                    max_cost = cost

        return max_cost
