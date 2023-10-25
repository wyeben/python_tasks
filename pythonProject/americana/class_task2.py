
def check_pattern(word1):
    pattern = ''
    i = 0

    while i < len(word1):
        if word1 == pattern * (len(word1) // ):
            i += 1
        else:
            return False

    return True


input1 = "abab"
input2 = "aba"
input3 = "abcabcabc"
print(check_pattern(input1))
print(check_pattern(input2))
print(check_pattern(input3))
