# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 10:24:07 2022

@author: agher
"""

from tree import BinaryTree

tree = BinaryTree.randomTree(4)


def count_nodes(tree):
    if not tree:
        return 0
    return count_nodes(tree.sx) + count_nodes(tree.dx) + 1


def get_nodes_at_depth(tree, depth, nodes=[]):
    if depth == 0:
        nodes.append(tree.valore)
        return nodes
    if tree.sx:
        get_nodes_at_depth(tree.sx, depth - 1, nodes)
    if tree.dx:
        get_nodes_at_depth(tree.dx, depth - 1, nodes)
    return nodes


print(tree)
size = count_nodes(tree)
print(f"Size of tree: {size}")

nodes_at_depth = get_nodes_at_depth(tree, 1)
print(nodes_at_depth)


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
