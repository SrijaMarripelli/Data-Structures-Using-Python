class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Inserts a new node with the given value into the binary search tree"""
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = new_node
                        return
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        return
                    else:
                        current = current.right

    def search(self, value):
        """Searches for a node with the given value in the binary search tree"""
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def inorder_traversal(self, node):
        """Performs an inorder traversal of the binary search tree"""
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.value)
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        """Performs a preorder traversal of the binary search tree"""
        if node is not None:
            print(node.value)
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        """Performs a postorder traversal of the binary search tree"""
        if node is not None:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value)

# create a new binary search tree
bst = BinarySearchTree()

# insert nodes into the tree
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(14)
bst.insert(4)
bst.insert(7)
bst.insert(13)

# search for a node in the tree
print(bst.search(6))  # Output: True
print(bst.search(12))  # Output: False

# perform inorder traversal of the tree
bst.inorder_traversal(bst.root)  # Output: 1 3 4 6 7 8 10 13 14

# perform preorder traversal of the tree
bst.preorder_traversal(bst.root)  # Output: 8 3 1 6 4 7 10 14 13

# perform postorder traversal of the tree
bst.postorder_traversal(bst.root)  # Output: 1 4 7 6 3 13 14 10 8

