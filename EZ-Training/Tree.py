class Node:
    def __init__(self, data):
        self.left = None
        self.val = data
        self.right = None

def preorder(root):
    if root == None:
        return
    print(root.val,end=" ")
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val,end=" ")

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.val,end=" ")
    inorder(root.right)

if __name__=="__main__":
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)

    root.right.left = Node(6)
    root.right.right = Node(7)
    # print(root.val,root.left.val,root.right.val)

print("\nPreorder : ")
preorder(root)
print("\nPostorder : ")
postorder(root)
print("\nInorder : ")
inorder(root)