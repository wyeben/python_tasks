def can_transform(word1, word2):
    def process_word(word):
        result = []
        for char in word:
            if char == '#':
                if result:
                    result.pop()
            else:
                result.append(char)
        return ''.join(result)

    words1 = process_word(word1)
    words2 = process_word(word2)

    return words1 == words2


wordz1 = 'a#b#d#pqrs#'
wordz2 = 'ac#d##pqr'

result = can_transform(wordz1, wordz2)
print(result)
