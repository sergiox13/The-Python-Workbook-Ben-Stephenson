words = []
word = input('Enter a word (empty to exit): ')

while word:
    words.append(word)
    word = input('Enter a word (empty to exit): ')

result = []
for word in words:
    if word not in result:
        result.append(word)

print(result)

#temp = set(words)
#temp = sorted(temp)
#print(temp)