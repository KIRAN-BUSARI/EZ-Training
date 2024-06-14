vowels = 'aeiou'
num_sent = int(input("Enter the number of sentences: "))
for _ in range(num_sent):
    sent = input("Enter a sentence: ")
    vowel_count = {v: 0 for v in vowels}
    for char in sent.lower():
        if char in vowel_count:
            vowel_count[char] += 1
    max_freq = max(vowel_count.values())
    most_freq = [vowel for vowel, count in vowel_count.items() if count == max_freq and count > 0]
    most_freq.sort()
    res = ''.join(most_freq)
    print(res)