number = int(input())
words = []
for i in range(number):
    words.append(input())

counter = [0]*len(words)
c = 0
for word in words:
    idx = words.index(word)
    if idx == c:
        counter [idx] = word.count(word)
    c = c + 1

counter = [str(i for i in counter if i)]
print(len(counter))
print(" ".join(counter))