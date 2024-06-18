#Quick Sort


def divide(L,Low,High):
    P=L[High]
    Pi=High
    j=Low-1
    for i in range (Low,High):
        if L[i]<=P:
            j+=1
            L[i],L[j]=L[j],L[i]
    j+=1
    L[j],L[Pi]=L[Pi],L[j]
    Pi=j
    return Pi

def Quick_Sort(L,Low,High):
    if Low<High:
        pi=divide(L,Low,High)
        Quick_Sort(L,Low,pi-1)
        Quick_Sort(L,pi+1,High)
    return    


if __name__=="__main__":
    L=list(map(int,input().split())) #4 7 8 3 2 9 1 5
    low=0
    high= len(L)-1
    Quick_Sort(L,low,high)

    print("Sorted Array = ",L)