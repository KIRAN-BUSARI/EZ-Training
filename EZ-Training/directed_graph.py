g=[
    [0,6,4,5,False,False],
    [False,0,False,False,-1,False],
    [False,-2,0,False,3,False],
    [False,False,-2,0,False,-1],
    [False,False,False,False,0,3],
    [False,False,False,False,False,0]
]
# d={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F'}
e=[]
for i  in range(len(g)):
    for j in range(len(g[i])):
        if g[i][j]!=False and g[i][j]!=0:
            e.append(tuple((i,j)))
print(e)
di={}
for i in range(len(g)):
    di[i]=float('inf')
di[0]=0
print(di)
for i in range(len(g)-1):
    for j in e:
        new_di=di[j[0]]+g[j[0]][j[1]]
        if di[j[1]]>new_di:
            di[j[1]]=new_di