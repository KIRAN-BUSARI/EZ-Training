def is_Prime(n):
    flag = 0
    if n < 1:
        flag = 1
    elif n == 1:
        flag = 0
    else:
        for i in range(2,(n//2)+1):
            if n % i == 0:
                flag = 1
                break
    if flag == 0:
        return True
    else:
        return False

N = int(input("Enter Number : "))
if is_Prime(N):
    print("Prime")
else:
    print("Not Prime")
