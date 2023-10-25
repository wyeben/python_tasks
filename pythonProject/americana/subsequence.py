def subsequence(word1, word2):
    i, j = 0, 0

    while i < len(word1) and j < len(word2):
        if word1[i] == word2[j]:
            i += 1
        j += 1

    return i == len(word1)


def subsequence1(y, t):
    i = 0
    r = 0
    for i in range(len(y)):
        for r in range(len(t)):
            if y[i] == t[r]:
                i += 1
            r += 1
    return i == len(y)


words1 = 'bce'
words2 = 'abcde'
words3 = 'met'
words4 = 'stream'
words5 = 'stem'
words6 = 'stream'
print(subsequence1(words1, words2))
print(subsequence1(words3, words4))
print(subsequence1(words5, words6))
