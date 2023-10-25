
def check_pattern(word1):
    pattern = word1[0]
    i = 1

    while i < len(word1):
        if word1[i] == pattern:
            i += 1
        else:


    return i == len(word1)


input1 = "abab"
input2 = "aba"
input3 = "abcabcabc"
print(check_pattern(input1))
print(check_pattern(input2))
print(check_pattern(input3))
