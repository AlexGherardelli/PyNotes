class Node:
    """ Binary tree. """

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self):
        return f"Node({self.data})"

    def __str__(self):
        return f'{self.data}, left: {self.left}, right: {self.right}'

    def search(self, target):
        if self.data == target:
            print("Found it")
            return self
        if self.left and self.data > target:
            print("Found it")
            return self.left.search(target)
        if self.right and self.data < target:
            print("Found it")
            return self.right.search(target)

        print("Not Found")

    def traverse_pre_order(self):
        print(self.data)
        if self.left:
            self.left.traverse_pre_order()

        if self.right:
            self.right.traverse_pre_order()

    def traverse_in_order(self):

        if self.left:
            self.left.traverse_in_order()

        print(self.data)

        if self.right:
            self.right.traverse_in_order()

    def traverse_post_order(self):
        if self.left:
            self.left.traverse_post_order()

        if self.right:
            self.right.traverse_post_order()

        print(self.data)


class Tree:
    """ Wrapper class for Tree"""

    def __init__(self, root, name):
        self.root = root
        self.name = name

    def __repr__(self):
        return f'Tree({self.root}, {self.name})'

    def __str__(self):
        return f'name: {self.name},\n tree:\n {self.root}'

    def search(self, target):
        return self.root.search(target)

    def traverse_pre_order(self):
        return root.traverse_pre_order()

    def traverse_in_order(self):
        return root.traverse_in_order()

    def traverse_post_order(self):
        return root.traverse_post_order()


# Building Tree
tree = Tree(Node(50), 'Tree Traversals')
tree.root.left = Node(25)
tree.root.right = Node(75)
tree.root.left.left = Node(10)
tree.root.left.right = Node(35)
tree.root.left.right.left = Node(30)
tree.root.left.right.right = Node(42)
tree.root.left.left.left = Node(5)
tree.root.left.left.right = Node(13)

print(tree)
