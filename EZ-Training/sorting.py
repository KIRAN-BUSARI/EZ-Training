class node_data:
    def __init__(self,Node,key):
        self.node=Node
        self.key=key
        self.left=None
        self.right=None
def topview(root):
    temp=node_data(root,0)
    q=[temp]
    q.append(None)
    
    key_d={}
    
    while len(q)!=0:
        curr=q.pop(0)
    
        if curr==None:
            if len(q)==0:
                break
            else:
                print()
                q.append(None)
        else:
            if curr.key not in key_d.keys():
                key_d[curr.key]=curr.node.value
            #print(curr.value,end='')
            if curr.node.left!=None:
                temp=node_data(curr.node.left,curr.key-1)
                q.append(temp)
            if curr.right!=None:
                temp=node_data(curr.node.right,curr.key+1)
                q.append(temp)
        for i in sorted(d):
            print(d[i].value)
        print(key_d)

if __name__=="__main__":
    root = node(1)

    root.left = node(2)
    root.right = node(3)

    root.left.left=node(4)
    root.left.right=node(5)

    root.right.left=node(6)
    root.right.right=node(7)
    
    root.right.left.right=node(8)
    root.right.left.left=node(9)
    
    root.right.right.left=node(10)
    root.right.right.right=node(11)
    
    root.right.right.left.left=node(12)
    root.right.right.left.right=node(13)
    topview(root)