def pigLatin(s):

    words = s.split(' ')
    result = []

    for word in words:

        if word[0] in 'aeiou':
            result.append(word + 'way')
        elif word[0] not in 'aeiou':
            c = 0
            for l in word:
                if l not in 'aeiou':
                    c += 1
                else:
                    break
            result.append(f'{word[c:]}{word[:c]}ay')

    return result

s = input('Enter a words: ').lower()

print(pigLatin(s))