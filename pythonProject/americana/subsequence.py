def subsequence(word1, word2):
    for char in word1:
        for letter in word2:
            if char == letter:
                return True
            else:
                return False


words1 = 'bcd'
words2 = 'abcde'
words3 = 'met'
words4 = 'stream'
words5 = 'stem'
words6 = 'stream'
print(subsequence(words1, words2))
print(subsequence(words3, words4))
print(subsequence(words5, words6))
