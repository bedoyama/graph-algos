from graph_algos.algos.bellman_ford import BellmanFord
from graph_algos.algos.dijkstras import Dijkstras
from graph_algos.entities.graph.graph import Graph


class AllPairsCost:
    def computeUsingBellmanFord(g: Graph) -> list:
        last: list = []
        bfComputer = BellmanFord()
        for n in range(g.num_nodes):
            last.append(bfComputer.compute(g, n))
        return last
    
    def computeUsingDijkstras(g: Graph) -> list:
        last: list = []
        dComputer = Dijkstras()
        for n in range(g.num_nodes):
            last.append(dComputer.compute(g, n))
        return last

    def compute(g: Graph, use_dijkstras: bool = True) -> list:
        if use_dijkstras:
            return AllPairsCost.computeUsingDijkstras(g)
        else:
            return AllPairsCost.computeUsingBellmanFord(g)