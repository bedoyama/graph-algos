import queue
from typing import Union

from graph_algos.entities.graph import Graph
from graph_algos.entities.node import Node
from graph_algos.utils.graph_bfs_utils import GraphBFSUtils


class PGState:
    def __init__(self, guards_left: int = 3, prisoners_left: int = 3,
                 boat_side: str = "L"):
        self.guards_left = guards_left
        self.prisoners_left = prisoners_left
        self.boat_side = boat_side

    def __str__(self) -> str:
        return (f"{self.guards_left},{self.prisoners_left},{self.boat_side}")


def pg_result_of_move(state: PGState, num_guards: int,
                      num_prisoners: int) -> Union[PGState, None]: 
    if num_guards < 0 or num_prisoners < 0:
        return None
    if num_guards + num_prisoners == 0:
        return None
    if num_guards + num_prisoners > 2:
        return None

    G_L: int = state.guards_left
    G_R: int = (3 - state.guards_left)
    P_L: int = state.prisoners_left
    P_R: int = (3 - state.prisoners_left)
    if state.boat_side == "L":
        G_L -= num_guards
        G_R += num_guards
        P_L -= num_prisoners
        P_R += num_prisoners
        new_side: str = "R"
    else:
        G_L += num_guards
        G_R -= num_guards
        P_L += num_prisoners
        P_R -= num_prisoners
        new_side = "L"

    if G_L < 0 or P_L < 0 or G_R < 0 or P_R < 0:
        return None
    if G_L > 0 and G_L < P_L:
        return None
    if G_R > 0 and G_R < P_R:
        return None
    return PGState(G_L, P_L, new_side)

def pg_neighbors(state: PGState) -> list: 
    neighbors: list = []
    for move in [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]:
        n: Union[PGState, None] = pg_result_of_move(state, move[0], move[1])
        if n is not None:
            neighbors.append(n)
    return neighbors

def create_prisoners_and_guards() -> Graph: 
    indices: dict = {}
    next_node: queue.Queue = queue.Queue()
    g: Graph = Graph(0, undirected=True)

    initial_state: PGState = PGState(3, 3, "L")
    initial: Node = g.insert_node(label=initial_state)
    next_node.put(initial.index)
    indices[str(initial_state)] = initial.index

    while not next_node.empty():
        current_ind: int = next_node.get()
        current_node: Node = g.nodes[current_ind]
        current_state = current_node.label

        neighbors: list = pg_neighbors(current_state)
        for state in neighbors:
            state_str: str = str(state)
            if not state_str in indices:
                new_node: Node = g.insert_node(label=state)
                indices[state_str] = new_node.index
                next_node.put(new_node.index)
            new_ind: int = indices[str(state)]
            g.insert_edge(current_ind, new_ind, 1.0)

    return g

def pg_state_to_index_map(g: Graph) -> dict: 
    state_to_index: dict = {}
    for node in g.nodes:
        state: str = str(node.label)
        state_to_index[state] = node.index
    return state_to_index

def solve_pg_bfs(): 
    g: Graph = create_prisoners_and_guards()

    state_to_index: dict = pg_state_to_index_map(g)
    start_index: int = state_to_index["3,3,L"]
    end_index: int = state_to_index["0,0,R"]

    last: int = GraphBFSUtils.breadth_first_search(g, start_index)

    current: int = end_index
    path_reversed: list = []
    while current != -1:
        path_reversed.append(current)
        current = last[current]

    if path_reversed[-1] != start_index:
        print("No solution")
        return

    for i, n in enumerate(reversed(path_reversed)):
        print(f"Step {i}: {g.nodes[n].label}")
