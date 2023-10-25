def subsequence(word1):
    for r in word1:
        if r.startswith('a') and r.endswith('b'):
            return True
    return False


def subsequence1(word1):
    i = 0

    while i in word1:
        if word1[i] == word1[i]:
            i += 1
        i += 1

    return i == word1


input1 = "abab"
input2 = "aba"
input3 = "abcabcabc"
print(subsequence1(input1))
print(subsequence1(input2))
print(subsequence1(input3))
