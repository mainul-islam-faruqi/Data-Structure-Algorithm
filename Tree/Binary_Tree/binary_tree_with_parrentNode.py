class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
    
    def __repr__(self):
        return repr(self.data)
    
    def add_left(self, node):
        self.left = node

        if node is not None:
            node.parent = self

    def add_right(self, node):
        self.right = node

        if node is not None:
            node.parent = self


def create_tree():
    two = TreeNode(2)
    seven = TreeNode(7)
    nine = TreeNode(9)
    two.add_left(seven)
    two.add_right(nine)
    one = TreeNode(1)
    six = TreeNode(6)
    seven.add_left(one)
    seven.add_right(six)
    five = TreeNode(5)
    ten = TreeNode(10)
    six.add_left(five)
    six.add_right(ten)
    eight = TreeNode(8)
    nine.add_right(eight)
    three = TreeNode(3)
    four = TreeNode(4)
    eight.add_left(three)
    eight.add_right(four)
    # now return the root node
    return two

root = create_tree()
print(root.left.parent)
