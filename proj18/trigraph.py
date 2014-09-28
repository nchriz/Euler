class Node:
    def __init__(self, n):
        self.n = n
        self.next = []

    def addNode(self, node):
        self.next.append(node)

    def largestEdge(self):
        return self.next[0] if self.next[0].value() > self.next[1].value() else self.next[1]

    def value(self):
        return self.n

    def check(self):
        if not self.next:
            return False
        return True
