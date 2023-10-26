def check_pattern(word1):
    pattern = ''
    i = 0

    while i < len(word1):
        pattern += word1[i]
        repeated_pattern = pattern * (len(word1) // len(pattern))
        if repeated_pattern == word1:
            return True
        i += 1
    return False


input1 = "abab"
input2 = "aba"
input3 = "abcabcabc"
print(check_pattern(input1))
print(check_pattern(input2))
print(check_pattern(input3))

