from tree import BinaryTree


new_tree = BinaryTree.randomTree(6)


def height(root):
    if not root:
        return 0
    else:
        return max(height(root.sx), height(root.dx)) + 1


def level_width(root, level):
    if not root:
        return 0
    if level == 1:
        return 1
    else:
        return (level_width(root.sx, level - 1) + level_width(root.dx, level - 1))


print(height(new_tree))
print(level_width(new_tree, 4))
