def subsequence(word1):
    for r in word1:
        if r.startswith('a') and r.endswith('b'):
            return True
    return False


input1 = "abab"
input2 = "aba"
input3 = "abcabcabc"
print(subsequence(input1))
print(subsequence(input2))
print(subsequence(input3))
