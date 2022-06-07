# -*- coding: utf-8 -*-
from tree import BinaryTree


class Tree:
    """Basic binary tree"""

    def __init__(self, val, right=None, left=None):
        self.right = right
        self.left = left
        self.val = val

    def __str__(self):
        return f"{self.val} | Right Child: {self.right} | Left Child: {self.left}"

# Costructing tree
# tree = BinaryTree(10)
# tree.left = BinaryTree(20, 3, 5)


# %% TRANSVERING
tree = BinaryTree.randomTree(6)


def pre_order(root):
    """Binary tree: pre order transversal."""
    print(root.valore)

    if root.sx:
        pre_order(root.sx)

    if root.dx:
        pre_order(root.dx)


def in_order(root):
    """Binary tree: in order transversal."""

    if root.sx:
        in_order(root.sx)

    print(root.valore)

    if root.dx:
        in_order(root.dx)


def post_order(root):
    """Binary tree: post prder transversal."""
    if root.sx:
        post_order(root.sx)
    if root.dx:
        post_order(root.dx)
    print(root.valore)


print(tree)

print("\n Pre order transversal")
pre_order(tree)

print("\n In order transversal")
in_order(tree)

print("\n Post order transversal")
post_order(tree)

# %% GET HEIGHT AND WIDTH OF TREE


def tree_height(root):
    """Get tree height: number of nodes between root and leaf."""
    if not root:
        return 0
    else:
        return max(tree_height(root.sx), tree_height(root.dx)) + 1


def level_width(root, level):
    """Get level height: number of notes in a certain level."""
    if root is None:
        return 0
    if level == 1:
        return 1
    else:
        return (level_width(root.sx, level - 1) +
                level_width(root.dx, level - 1))


def tree_width(root):
    """Get max width: max level width in a tree."""
    max_width = 0
    height = tree_height(root)
    for i in range(height + 1):
        width = level_width(root, i)
        if width > max_width:
            max_width = width
    return max_width


print(f"Tree height: {tree_height(tree)}\n")
print(f"Tree width: {tree_width(tree)}\n")


# %% DIAMETER


def tree_diameter(root):
    """Get tree diameter: longest path between leafs."""
    if not root:
        return 0
    else:
        diameter_left = tree_diameter(root.sx)
        diameter_right = tree_diameter(root.dx)

        height_left = tree_height(root.sx)
        height_right = tree_height(root.dx)

        # il percorso massimo che passa per la radice Ã¨ la loro somma +1
        rad = height_left + height_right + 1

        return max(rad, diameter_left, diameter_right)


print(f"Tree diameter: {tree_diameter(tree)}")
