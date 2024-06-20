class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

def levelOrder(root):
    Q = [root]
    Q.append(None)
    while len(Q) != 0:
        current = Q.pop(0)
        if current is None:
            if len(Q) == 0:
                break
            else:
                print()
                Q.append(None)
        else:
            print(current.data, end=" ")
            if current.left is not None:
                Q.append(current.left)
            if current.right is not None:
                Q.append(current.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    
    root.left.left = Node(4)
    root.left.right = Node(5)

    root.right.left = Node(6)
    root.right.right = Node(7)

    root.left.left.left = Node(8)
    root.left.left.right = Node(9)

    root.right.right.left = Node(10)
    root.right.right.right = Node(11)

levelOrder(root)