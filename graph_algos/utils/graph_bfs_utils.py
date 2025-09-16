import queue

from graph_algos.entities.graph import Graph
from graph_algos.entities.node import Node


class GraphBFSUtils:
    @staticmethod
    def breadth_first_search(g: Graph, start: int) -> list: 
        seen: list = [False] * g.num_nodes
        last: list = [-1] * g.num_nodes
        pending: queue.Queue = queue.Queue()

        pending.put(start)
        seen[start] = True

        while not pending.empty():
            index: int = pending.get()
            current: Node = g.nodes[index]

            for edge in current.get_edge_list():
                neighbor: int = edge.to_node
                if not seen[neighbor]:
                    pending.put(neighbor)
                    seen[neighbor] = True
                    last[neighbor] = index

        return last
