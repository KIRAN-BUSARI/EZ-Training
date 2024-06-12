# Happy number
def squareOfNumber(n):
    rem = 0
    sum = 0
    while n != 0:
        rem = n % 10
        sum += (rem * rem)
        n //= 10
    return sum

n = int(input("Enter a number: "))
ans = squareOfNumber(n)
while True:
    if ans >= 0 and ans < 10:
        if ans == 1:
            print("Happy Number")
            break
        else:
            print("Not Happy Number")
            break