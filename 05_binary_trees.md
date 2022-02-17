# Trees

## TODO
- Creating a binary tree
- Traversing a tree
    - Pre-order
    - Post-order
    - In-order
- Find height, width, diameter of binary tree

- File searching as tree
    - OS methods: os.listdir, os.walk, os.path

- Game Trees (opt)
    - Examples

## Binary Trees



### Create a binary tree
```python
# Create a class

class BinaryTree:
    def __init__(self, value, left = None, left = right):
        self.left = left
        self.right = right
        self.value = value
```


### Transversing a tree

**Pre-order traversing**
```python
def preorder(tree):
    print(tree.value)
    if tree.left:
        preorder(tree.left)
    if tree.right:
        preorder(tree.right)
```

**In-order trasversing**
```python
def inorder(tree)":
    if tree.left:
        inorder(tree.left)
    print(tree.value)
    if tree.right:
        inorder(tree.right)

```

**Post-order traversing**
```python
def postorder(tree):
    if tree.left:
        postorder(tree.left)
    if tree.right:
        postorder(tree.right)
    print(tree.value)

```

## Get information about binary tree

**Height**



```python
# Method 1
def height(tree, h = 0):
    left_height = height(tree.left, h + 1) if tree.left else h
    right_height = height(tree.right, h + 1) if tree.right else h
    return max(left_height, right_height)


# Method 2
def tree_height(root):
    """Get tree height: number of nodes between root and leaf."""
    if not root:
        return 0
    else:
        return max(tree_height(root.sx), tree_height(root.dx)) + 1
```

**Level width**
Explaination: TODO

```python
def level_width(root, level):
    """Get level height: number of notes in a certain level."""
    if root is None:
        return 0
    if level == 1:
        return 1
    else:
        return (level_width(root.sx, level - 1) +
                level_width(root.dx, level - 1))
```


**Max width**
Explaination: TODO

```python
def tree_width(root):
    """Get max width: max level width in a tree."""
    max_width = 0
    height = tree_height(root)
    for i in range(height + 1):
        width = level_width(root, i)
        if width > max_width:
            max_width = width
    return max_width
```

**Diameter**
Explaination: TODO

```python
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

```

**Number of nodes**
The function below counts the number of nodes in a binary tree.
It initiate a counter and if the tree doesn't exist, immediately returns it. Otherwise, keeps exploring the tree and adding the number of nodes found to the counter. 

```python
def get_nodes(tree, count = 0):
    if not tree:
        return count
    return get_nodes(tree.sx) + get_nodes(tree.dx) + 1
```

**Get nodes at depth**
```python
def get_nodes_at_depth(tree, depth, nodes=[]):
    if depth == 0:
        nodes.append(tree.valore)
        return nodes
    if tree.sx:
        get_nodes_at_depth(tree.sx, depth - 1, nodes)
    if tree.dx:
        get_nodes_at_depth(tree.dx, depth - 1, nodes)
    return nodes
```


## N-Ary Trees

## Filesystem as tres
**Remember: all methods are easily available on the documentatio**


```python
import os

def explore(folder, ext, lst = []):
    """
    This method recursively search into a folder and its subfolders and appends all files found to a list
    """
    for items in os.listdir(folder):
        # create fullpath, otherwise is_dir and is_file will fail
        fullpath = folder + "/" + item # NOTE: there is a method os.path.join, but it can fail in Windows
        if os.path.isfile(fullpath):
            # Do somethign with file'
            lst.append(fullpath)
        elif os.path.isdir(fullpath):
            # Recursive call!
            explore(fullpath, ext, lst)
    return lst

```


