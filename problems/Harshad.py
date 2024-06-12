def harshad(n):
    sum = 0
    temp = n
    while temp != 0:
        sum += temp % 10
        temp //= 10
    return n % sum == 0

n = int(input("Enter a number: "))
print(harshad(n))

if harshad(n):
    print("Harshad Number")
else:
    print("Not Harshad Number")

