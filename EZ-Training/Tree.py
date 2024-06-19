class Node:
    def __init__(self, data):
        self.left = None
        self.val = data
        self.right = None

def preorder(root):
    if root == None:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)

def inorder(root):
    if root == None:
        return
    inorder(root.right)
    print(root.val)
    inorder(root.left)

if __name__=="__main__":
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)

    root.right.left = Node(6)
    root.right.right = Node(7)
    # print(root.val,root.left.val,root.right.val)

# preorder(root)
# postorder(root)
inorder(root)