
class Node:

    def __init__(self, value, left=None, right=None):

        self.value = value
        self.left = left
        self.right = right

        self.height = 0

    def __repr__(self):
        return str(self.value)


def print_tree(tree_root, level=0):

    if tree_root is not None:
        print_tree(tree_root.left, level+1)
        print(' '*4*level, '->', tree_root.value)
        print_tree(tree_root.right, level+1)


class Tree:

    def __init__(self, root):
        self.root = root
        self.add_element_queue = [self.root]

    def add_element(self, value):

        node = Node(value)

        parent = self.add_element_queue[0]
        if parent.left is None:
            parent.left = node
            self.add_element_queue.append(node)
        else:
            parent.right = node
            self.add_element_queue.pop(0)
            self.add_element_queue.append(node)


start = Node(5)
tree = Tree(start)

tree.add_element(1)
tree.add_element(7)
tree.add_element(-2)
tree.add_element(3)
tree.add_element(-3)
tree.add_element(-6)
tree.add_element(2)
tree.add_element(67)
tree.add_element(-3)
tree.add_element(3)
tree.add_element(-65)
tree.add_element(-3)
tree.add_element(12)
# print_tree(tree.root)

path_cost_map = {0: 0}

backup_counter = 0

def find_paths(root, sum, path_cost_map, level=1):

    global backup_counter

    if root is None:
        return 0

    total_count = 0
    path_cost = path_cost_map[level-1] + root.value
    required_sum = path_cost - sum

    for key, value in path_cost_map.items():
        if value == required_sum:
            print(key, root.value)
            total_count += 1
            backup_counter += 1

    path_cost_map[level] = path_cost

    left_count = find_paths(root.left, sum, path_cost_map, level+1)
    rigth_count = find_paths(root.right, sum, path_cost_map, level+1)

    path_cost_map.pop(level)
    total_count += left_count + rigth_count
    return total_count


result = find_paths(tree.root, 6, path_cost_map)

print("done")