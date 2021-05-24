


class Node:

    def __init__(self, value:int, children:list=[]):

        self.value = value
        self.children = children

def inorder_print(node:Node):
    
    if not node:
        return
    
    inorder_print(node.children[0])
    if node.value:
        print(node.value)
    inorder_print(node.children[1])
  

def create_tree(array:list) -> Node:

    if len(array) == 0:
        return None

    mid_index = len(array)//2 


    left_child = create_tree(array[:mid_index])
    right_child = create_tree(array[mid_index+1:])
    node = Node(array[mid_index], [left_child, right_child])

    return node


def main():


    array = [1,2,3,4,5,6,7,8,9]

    tree = create_tree(array)

    inorder_print(tree)


if __name__ == "__main__":
    main()
