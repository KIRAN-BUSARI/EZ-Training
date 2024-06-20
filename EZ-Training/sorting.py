class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class node_data:
    def __init__(self, Node, key):
        self.node = Node
        self.key = key

def topview(root):
    if root is None:
        return
    key_d = {}
    q = [node_data(root, 0)]
    while q:
        curr = q.pop(0)
        if curr.key not in key_d:
            key_d[curr.key] = curr.node.value
        if curr.node.left:
            q.append(node_data(curr.node.left, curr.key - 1))
        if curr.node.right:
            q.append(node_data(curr.node.right, curr.key + 1))
    
    print(key_d)
    for key in sorted(key_d):
        print(key_d[key])

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.left.left = Node(9)
    root.right.right.left = Node(10)
    root.right.right.right = Node(11)
    root.right.right.left.left = Node(12)
    root.right.right.left.right = Node(13)
    
    topview(root)