from node import TreeNode

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def recursive_sum(lst):
    if not lst:
        return 0
    return lst[0] + sum(lst[1:])

def find_maximum(root):
    if not root:
        return -1
    else:
        return max((root.value, find_maximum(root.left), find_maximum(root.right)))

def tree_to_list(root):
    if root is None:
        return []
    else:
        return [root.value] + tree_to_list(root.left) + tree_to_list(root.right)

def equals(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.value != root2.value:
        return False
    return equals(root1.left, root2.left) and equals(root1.right, root2.right)

def build_tree(value, height):
    '''Build a tree where each value is value of the given height.'''
    if height == 0:
        return None
    return TreeNode(value, build_tree(value, height - 1), build_tree(value, height - 1))

def get_height(node):
    '''Return the height of the tree.'''
    if not node:
        return 0
    return 1 + max(get_height(node.left), get_height(node.right))

def sum_tree(node):
    if node is None:
        return 0
    else:
        return sum_tree(node.left) + sum_tree(node.right) + node.value

def print_all(node):
    if node is None:
        return
    else:
        print node.value
        print_all(node.left)
        print_all(node.right)

def build_coinflip_tree(k, flips=''):
    if k == 0:
        return None
    else:
        return TreeNode(flips, build_coinflip_tree(k - 1, flips + 'H'), build_coinflip_tree(k - 1, flips + 'T'))
        # node.left = build_coinflip_tree(node, k-1)
        # node.right = build_coinflip_tree(node, k-1)

if __name__ == '__main__':
    # build a tree
    #     1
    #    / \
    #   2   3
    #  /
    # 4
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)
    t1.left.left = TreeNode(4)

    # build a tree
    #     1
    #    / \
    #   2   3
    #  /   /
    # 4   5
    t2 = TreeNode(1)
    t2.left = TreeNode(2)
    t2.right = TreeNode(3)
    t2.left.left = TreeNode(4)
    t2.right.left = TreeNode(5)

    print find_maximum(t1)    # 4
    print find_maximum(t2)    # 5
    print equals(t1, t2)      # False
    print get_height(t1)      # 3
    print sum_tree(t1)
    print sum_tree(t2)
    print_all(t1)
    print_all(t2)
    tree = build_coinflip_tree(3)
    print_all(tree)

    #     2
    #    / \
    #   2   2
    # /  \   / \
    # 2   2  2  2
