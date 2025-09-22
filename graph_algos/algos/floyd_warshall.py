import math
from typing import Union
from graph_algos.entities.graph.edge import Edge
from graph_algos.entities.graph.graph import Graph


class FloydWarshall:
    @staticmethod
    def compute(g: Graph) -> list: 
        N: int = g.num_nodes
        cost: list = [[math.inf] * N for _ in range(N)]
        last: list = [[-1] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if i == j:
                    cost[i][j] = 0.0
                else:
                    edge: Union[Edge, None] = g.get_edge(i, j)
                    if edge is not None:
                        cost[i][j] = edge.weight
                        last[i][j] = i

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if cost[i][j] > cost[i][k] + cost[k][j]:
                        cost[i][j] = cost[i][k] + cost[k][j]
                        last[i][j] = last[k][j]
        return last
