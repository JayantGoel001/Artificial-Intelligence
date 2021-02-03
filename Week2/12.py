class Tree:
    def __init__(self, data=0):
        self.left = None
        self.right = None
        self.data = data

def inorder(tree):
    if not tree:
        return

    inorder(tree.left)
    print(tree.data, end=" ")
    inorder(tree.right)


if __name__ == '__main__':
    root = Tree(1)
    root.left = Tree(2)
    root.right = Tree(3)
    root.left.left = Tree(4)
    root.left.right = Tree(5)
    root.right.left = Tree(6)
    root.right.right = Tree(7)

    inorder(root)