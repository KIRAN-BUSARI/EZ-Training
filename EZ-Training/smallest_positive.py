ar1 = [5,7,-10,-3,0,3,-5,1]

smallest_number = 1

ar1.remove(min(ar1))
for i in ar1:
    if i < smallest_number:
        smallest_number = i
    else:
        continue
print(i)