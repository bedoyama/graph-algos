from graph_algos.algos.bellman_ford import BellmanFord
from graph_algos.algos.dijkstras import Dijkstras
from graph_algos.entities.graph.graph import Graph


class AllPairsCost:
    @staticmethod
    def computeUsingBellmanFord(g: Graph) -> list:
        last: list = []
        for n in range(g.num_nodes):
            last.append(BellmanFord.compute(g, n))
        return last
    
    @staticmethod
    def computeUsingDijkstras(g: Graph) -> list:
        last: list = []
        for n in range(g.num_nodes):
            last.append(Dijkstras.compute(g, n))
        return last

    @staticmethod
    def compute(g: Graph, use_dijkstras: bool = True) -> list:
        if use_dijkstras:
            return AllPairsCost.computeUsingDijkstras(g)
        else:
            return AllPairsCost.computeUsingBellmanFord(g)