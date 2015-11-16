from node import TreeNode

def sum_digits(n):
    if n / 10 == 0:
        return n
    else:
        return n % 10 + sum_digits(n / 10)

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

def build_coinflip_tree(node, k):
    if k == 0:
        return
    else:
        node.left = build_coinflip_tree(node, k-1)
        node.right = build_coinflip_tree(node, k-1)

def reconstruct_tree(t, i, node=''):
    if node is None:
        return
    if t == '':
        return
    root = t[0]
    node = TreeNode(root)
    try:
        left_length = i.index(root)
    except:
        left_length = 0
    right_length = len(i) - left_length - 1
    if left_length != 0:
        node.left = pre_inorder(t[1:1+left_length], i[:left_length], node)
    if right_length != 0:
        node.right = pre_inorder(t[-right_length:], i[-right_length:], node)
    return node

def print_all(node):
    if node is None:
        return ''
    else:
        return node.value + ' ' + print_all(node.left) + ' ' + print_all(node.right)
