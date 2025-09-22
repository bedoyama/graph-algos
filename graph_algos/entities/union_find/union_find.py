from graph_algos.entities.union_find.union_find_node import UnionFindNode


class UnionFind:
    def __init__(self, num_sets: int): 
        self.nodes: list = [UnionFindNode(i) for i in range(num_sets)]
        self.set_sizes: list = [1 for i in range(num_sets)]
        self.num_disjoint_sets: int = num_sets

    def find_set(self, label: int) -> int: 
        if label < 0 or label >= len(self.nodes):
            raise IndexError

        current: UnionFindNode = self.nodes[label]
        while current.parent is not None:
            current = current.parent
        return current.label

    def are_disjoint(self, label1: int, label2: int) -> bool: 
        return self.find_set(label1) != self.find_set(label2)

    def union_sets(self, label1: int, label2: int): 
        set1_label: int = self.find_set(label1)
        set2_label: int = self.find_set(label2)
        if set1_label == set2_label:
            return

        if self.set_sizes[set1_label] < self.set_sizes[set2_label]:
            small = set1_label
            large = set2_label
        else:
            small = set2_label
            large = set1_label
            
        self.nodes[small].parent = self.nodes[large]
        self.set_sizes[large] += self.set_sizes[small]
        self.set_sizes[small] = 0
        self.num_disjoint_sets -= 1
