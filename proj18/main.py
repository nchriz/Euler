import trigraph
from trigraph import *

def checkGraph(node):
    if node.check():
        return checkGraph(node.largestEdge())
    return node.value()
    
def main():
    a1 = Node(3)
    a2 = Node(7)
    a3 = Node(4)
    a4 = Node(2)
    a5 = Node(4)
    a6 = Node(6)
    a7 = Node(8)
    a8 = Node(5)
    a9 = Node(9)
    a10 = Node(3)

    a1.addNode(a2)
    a1.addNode(a3)
    a2.addNode(a4)
    a2.addNode(a5)
    a3.addNode(a5)
    a3.addNode(a6)

    print checkGraph(a1)
    print "hej"

if __name__ == "__main__":
    main()
