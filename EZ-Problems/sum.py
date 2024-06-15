l=[2,4,3,5,6,3,4,6,7,1,2,5]
sum=max=0
for i in range(0,len(l)-2):
    sum=l[i]+l[i+1]+l[i+2]
    if max<sum:
        max=sumpos=1
        pos=1
print(max,l[pos],l[pos+1],l[pos+2])