class Node:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return "Node[" + self.val + "]"


class Edge:
    def __init__(self, a: Node, b: Node):
        self.a = a
        self.b = b

    def add(self, node: Node):
        if self.a is None:
            self.a = node
        elif self.b is None:
            self.b = node

    def __repr__(self):
        return "Edge[{}, {}".format(self.a, self.b)


class Graph:
    def __init__(self):
        self.edges = []
        self.nodes = []

    def grade(self, node: Node):
        c = 0
        for edge in self.edges:
            if edge.a == node or edge.b == node:
                c += 1
        return c
