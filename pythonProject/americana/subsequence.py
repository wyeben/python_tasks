def subsequence(word1, word2):
    i, j = 0, 0

    while i < len(word1) and j < len(word2):
        if word1[i] == word2[j]:
            i += 1
        j += 1

    return i == len(word1)


words1 = 'cde'
words2 = 'abcde'
words3 = 'met'
words4 = 'stream'
words5 = 'stem'
words6 = 'stream'
print(subsequence(words1, words2))
print(subsequence(words3, words4))
print(subsequence(words5, words6))
