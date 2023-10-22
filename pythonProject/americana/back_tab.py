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



