

class Node:

    def __init__(self, value:int, adjacent:list=[]):

        self.value = value
        self.adjacent = adjacent
        self.visited = False

def check_route(node_1:Node, node_2:Node):

    q1 = [node_1]
    q2 = [node_2]

    # bfs search on both ends

    while (len(q1) != 0 and len(q2) != 0):

        r1 = q1.pop(0)
        r2 = q2.pop(0)
        
        print("______________")
        print(r1.value)
        print(r2.value)

        if node_1 in r2.adjacent or node_2 in r1.adjacent:

            print(r1.value, r2.value)
            return True

        r1.visited = True
        r2.visited = True

        q1.extend([i for i in r1.adjacent if not i.visited])
        q2.extend([i for i in r2.adjacent if not i.visited])

    return False
 
def main():

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)

    n1.adjacent = [n2]
    n2.adjacent = [n3]
    n3.adjacent = [n4]
    n4.adjacent = [n5, n6]
    n5.adjacent = [n6]
    n6.adjacent = [n1, n2]

    result = check_route(n1, n4)
    print(result)

main()
