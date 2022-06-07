from tree import *

tree = n7


def get_height(tree):
    if not tree:
        return 0
    else:
        return max(get_height(tree.left), get_height(tree.right)) + 1
    
print(get_height(tree))


