S = "ASDGFDABCEABCDEF"
P = "ABCDEF"

# Print the index of P in S

for i in range(len(S)-len(P)+1):
    count = 0
    for j in range(len(P)):
        if S[i+j] == P[j]:
            count += 1
    if count == len(P):
        print(i)    