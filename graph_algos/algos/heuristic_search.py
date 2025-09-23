import math

from graph_algos.entities.graph.graph import Graph
from graph_algos.entities.graph.node import Node
from graph_algos.entities.pq.priority_queue import PriorityQueue


class HeuristicSearch:
    @staticmethod
    def euclidean_dist(x1: float, y1: float, x2: float, y2: float) -> float:
        return math.sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2))

    @staticmethod
    def greedy_search(g: Graph, h: list, start: int, goal: int) -> list: 
        visited: list = [False] * g.num_nodes
        last: list = [-1] * g.num_nodes
        pq: PriorityQueue = PriorityQueue(min_heap=True)

        pq.enqueue(start, h[start])
        while not pq.is_empty() and not visited[goal]:
            ind: int = pq.dequeue()
            current: Node = g.nodes[ind]
            visited[ind] = True

            for edge in current.get_edge_list():
                neighbor: int = edge.to_node
                if not visited[neighbor] and not pq.in_queue(neighbor):
                    pq.enqueue(neighbor, h[neighbor])
                    last[neighbor] = ind

        return last

    @staticmethod
    def a_star_search(g: Graph, h: list, start: int, goal: int) -> list: 
        visited: list = [False] * g.num_nodes
        last: list = [-1] * g.num_nodes
        cost: list = [math.inf] * g.num_nodes
        pq: PriorityQueue = PriorityQueue(min_heap=True)

        pq.enqueue(start, h[start])
        cost[start] = 0.0

        while not pq.is_empty() and not visited[goal]:
            ind: int = pq.dequeue()
            current: Node = g.nodes[ind]
            visited[ind] = True

            for edge in current.get_edge_list():
                neighbor: int = edge.to_node
                new_cost: float = cost[ind] + edge.weight

                if not visited[neighbor] and not pq.in_queue(neighbor):
                    pq.enqueue(neighbor, new_cost + h[neighbor])
                    last[neighbor] = ind
                    cost[neighbor] = new_cost
                elif pq.in_queue(neighbor) and new_cost < cost[neighbor]:
                    pq.update_priority(neighbor, new_cost + h[neighbor])
                    last[neighbor] = ind
                    cost[neighbor] = new_cost

        return last