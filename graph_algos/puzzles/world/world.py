import math
from graph_algos.entities.graph.graph import Graph
from graph_algos.entities.pq.priority_queue import PriorityQueue


class World:
    def __init__(self, g: Graph, start_ind: int, goal_ind: int):
        self.g = g
        self.start_ind = start_ind
        self.goal_ind = goal_ind

    def get_num_states(self) -> int:
        return self.g.num_nodes

    def is_goal(self, state: int) -> bool:
        return state == self.goal_ind

    def get_start_index(self) -> int:
        return self.start_ind

    def get_neighbors(self, state: int) -> set:
        return self.g.nodes[state].get_neighbors()

    def get_cost(self, from_state: int, to_state: int) -> float:
        if not self.g.is_edge(from_state, to_state):
            return math.inf
        return self.g.get_edge(from_state, to_state).weight

    def get_heuristic(self, state: int):
        pos1 = self.g.nodes[state].label
        pos2 = self.g.nodes[self.goal_ind].label
        return math.sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)
    
def astar_dynamic(w: World): 
    visited: dict = {}
    last: dict = {}
    cost: dict = {}
    pq: PriorityQueue = PriorityQueue(min_heap=True)
    visited_goal: bool = False

    start: int = w.get_start_index()
    visited[start] = False
    last[start] = -1
    pq.enqueue(start, w.get_heuristic(start))
    cost[start] = 0.0

    while not pq.is_empty() and not visited_goal:
        index: int = pq.dequeue()
        visited[index] = True
        visited_goal = w.is_goal(index)

        for other in w.get_neighbors(index):
            c: float = w.get_cost(index, other)
            h: float = w.get_heuristic(other)

            if other not in visited:
                visited[other] = False
                cost[other] = cost[index] + c
                last[other] = index
                pq.enqueue(other, cost[other] + h)
            elif cost[other] > cost[index] + c:
                cost[other] = cost[index] + c
                last[other] = index
                pq.update_priority(other, cost[other] + h)

    return last

    

