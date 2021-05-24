

class Node:

    def __init__(self, value:int, children:list=None, parent=None):

        self.value = value
        if children is None:
            children = []
        self.children = children
        self.parent = parent


    def __repr__(self):
        return str(self.value)

def create_tree(array:list, parent=None) -> Node:

    global check_node

    if not array:
        return None

    mid_index = len(array)//5 

    r = Node(array[mid_index], children=[None, None], parent=parent)

    left_child = create_tree(array[:mid_index], r)
    right_child = create_tree(array[mid_index+1:], r) 

    r.children[0] = left_child
    r.children[1] = right_child

    if r.value == 2:
        check_node = r

    return r


def inorder_parser(node):

    if node.children[0] is not None:
        return inorder_parser(node.children[0])

    else:
        return node.value

def inorder_print_tree(tree):

    if tree is None:
        return

    inorder_print_tree(tree.children[0])
    print(f"value : {tree.value},    left_child : {getattr(tree.children[0], 'value', None)},     right_child : {getattr(tree.children[1], 'value', None)}")
    inorder_print_tree(tree.children[1])


def check_successor(node):
    if node.parent.value > node.value:
        return node.parent.value

    else:
        return check_successor(node.parent)

check_node = None

def main():
            
    values = [1,2,3,4,5,6,7,8,9,10,11,12]

    tree_root = create_tree(values)

#    print("printing tree")

#    inorder_print_tree(tree_root)

#    print("finished printing tree")

    if check_node.children[1] is not None:
        result = inorder_parser(check_node.children[1])

    else:
        result = check_successor(check_node)

    print('result : ', result)

main()



