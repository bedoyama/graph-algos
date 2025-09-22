# Credit: Edsger W. Dijkstra
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

import math
from graph_algos.entities.graph.graph import Graph
from graph_algos.entities.pq.priority_queue import PriorityQueue


class Dijkstras:
    @staticmethod
    def compute(g: Graph, start_index: int) -> list: 
        cost: list = [math.inf] * g.num_nodes
        last: list = [-1] * g.num_nodes
        pq: PriorityQueue = PriorityQueue(min_heap=True)

        pq.enqueue(start_index, 0.0)
        for i in range(g.num_nodes):
            if i != start_index:
                pq.enqueue(i, math.inf)
        cost[start_index] = 0.0

        while not pq.is_empty():
            index: int = pq.dequeue()

            for edge in g.nodes[index].get_edge_list():
                neighbor: int = edge.to_node

                if pq.in_queue(neighbor):
                    new_cost: float = cost[index] + edge.weight
                    if new_cost < cost[neighbor]:
                        pq.update_priority(neighbor, new_cost)
                        last[neighbor] = index
                        cost[neighbor] = new_cost

        return last
