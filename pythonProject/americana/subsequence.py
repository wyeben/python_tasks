def subsequence(word1, word2):
    i, j = 0, 0

    while i < len(word1) and j < len(word2):
        if word1[i] == word2[j]:
            i += 1
        j += 1

    return i == len(word1)


def is_subsequence(word1, word2):
    return all(char in word2 for char in word1)


words1 = 'bce'
words2 = 'abcde'
words3 = 'met'
words4 = 'stream'
words5 = 'stem'
words6 = 'stream'
print(is_subsequence(words1, words2))
print(is_subsequence(words3, words4))
print(is_subsequence(words5, words6))
