import random
from typing import Union
from graph_algos.entities import pq
from graph_algos.entities.graph.edge import Edge
from graph_algos.entities.graph.graph import Graph
from graph_algos.entities.graph.node import Node
from graph_algos.entities.pq.priority_queue import PriorityQueue
from graph_algos.entities.union_find.union_find import UnionFind


class MinimumSpanningTree:
    @staticmethod
    def prims(g: Graph) -> Union[list, None]:
        pq: PriorityQueue = PriorityQueue(min_heap=True)
        last: list = [-1] * g.num_nodes
        mst_edges: list = []

        pq.enqueue(0, 0.0)
        for i in range(1, g.num_nodes):
            pq.enqueue(i, float('inf'))

        while not pq.is_empty():
            index: int = pq.dequeue()
            current: Node = g.nodes[index]

            if last[index] != -1:
                mst_edges.append(current.get_edge(last[index]))
            elif index != 0:
                return None

            for edge in current.get_edge_list():
                neighbor: int = edge.to_node
                if pq.in_queue(neighbor):

                    if edge.weight < pq.get_priority(neighbor):
                        pq.update_priority(neighbor, edge.weight)
                        last[neighbor] = index

        return mst_edges

    @staticmethod
    def kruskals(g: Graph) -> Union[list, None]:
        djs: UnionFind = UnionFind(g.num_nodes)
        all_edges: list = []
        mst_edges: list = []

        for idx in range(g.num_nodes):
            for edge in g.nodes[idx].get_edge_list():
                if edge.to_node > edge.from_node:
                    all_edges.append(edge)
        all_edges.sort(key=lambda edge: edge.weight)
        for edge in all_edges:
            if djs.are_disjoint(edge.to_node, edge.from_node):
                mst_edges.append(edge)
                djs.union_sets(edge.to_node, edge.from_node)

        if djs.num_disjoint_sets == 1:
            return mst_edges
        else:
            return None

    @staticmethod
    def randomized_kruskals(g: Graph) -> list:
        djs: UnionFind = UnionFind(g.num_nodes)
        all_edges: list = []
        maze_edges: list = []

        for idx in range(g.num_nodes):
            for edge in g.nodes[idx].get_edge_list():
                if edge.to_node > edge.from_node:
                    all_edges.append(edge)

        while djs.num_disjoint_sets > 1:
            num_edges: int = len(all_edges)
            edge_ind: int = random.randint(0, num_edges - 1)
            new_edge: Edge = all_edges.pop(edge_ind)

            if djs.are_disjoint(new_edge.to_node, new_edge.from_node):
                maze_edges.append(new_edge)
                djs.union_sets(new_edge.to_node, new_edge.from_node)

        return maze_edges
