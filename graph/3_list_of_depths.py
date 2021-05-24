

class Node:

    def __init__(self, value:int, children:list=[]):

        self.value = value
        self.children = children

class LlNode:

    def __init__(self, value:int, next_node=None):

        self.value = value
        self.next = next_node


def create_tree(array:list) -> Node:

    if not array:
        return None

    mid_index = len(array)//2
    
    left_child = create_tree(array[:mid_index])
    right_child = create_tree(array[mid_index+1:])

    r = Node(array[mid_index], [left_child, right_child])

    return r


def print_link_list(node:LlNode):

    while node:

        print(node.value)
        node = node.next


def find_depths(tree_root:Node) -> list:

    list_mapping = []

    queue = []
    queue.append(tree_root)

    level_counter = 0
    while len(queue) > 0:
        next_queue = []
        list_mapping.append(LlNode(None))
        while len(queue) > 0:

            r = queue.pop()
            
            next_queue.extend([i for i in r.children if i])
            
            ll_element = LlNode(r.value)
            ll_element.next = list_mapping[level_counter].next
            list_mapping[level_counter].next = ll_element

        
        level_counter += 1
        queue = next_queue

    return list_mapping
    
    
def main():
    
    values = [0,1,2,3,4,5,6,7,8,9]

    tree_root = create_tree(values)

    list_mappings = find_depths(tree_root)
    
    for i in list_mappings:
        print("list")
        print_link_list(i)


if __name__ == '__main__':
    main()
