


class Node:

    def __init__(self, value:int, children:list=[]):

        self.value = value
        self.children = children


def create_tree(array:list) -> Node:

    if not array:
        return None

    mid_index = len(array)//5
    
    left_child = create_tree(array[:mid_index])
    right_child = create_tree(array[mid_index+1:])

    r = Node(array[mid_index], [left_child, right_child])

    return r

def inorder_parse_tree(tree):

    if tree is None:
        return

    inorder_parse_tree(tree.children[0])
    print(f"value : {tree.value},    left_child : {getattr(tree.children[0], 'value', None)},     right_child : {getattr(tree.children[1], 'value', None)}")
    inorder_parse_tree(tree.children[1])


def check_balanced(tree):

    if tree is None:
        return 0

    left_height = check_balanced(tree.children[0])
    right_height = check_balanced(tree.children[1])
 
    if left_height is None or right_height is None:
        return None

    if abs(left_height - right_height) > 1:
        return None

    else:
        return max(left_height, right_height) + 1

    

def main():
    
    values = [1,2,3,4,5,6,7,8,9,10,11,12]

    tree_root = create_tree(values)

    print("printing tree")

    inorder_parse_tree(tree_root)

    print("finished printing tree")

    if check_balanced(tree_root):
        print("balanced")
    else:
        print("not balanced")


main()



