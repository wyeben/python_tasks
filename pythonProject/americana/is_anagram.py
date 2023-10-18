def is_anagram(s, t):
    if len(s) != len(t):
        return 'please words '

    s = s.lower()
    t = t.lower()

    char_count = {}

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in t:
        if char in char_count and char_count[char] > 0:
            char_count[char] -= 1
        else:
            return False

    return True


word1 = "anagram"
word2 = "aganram"
word3 = 'chair'
word4 = 'cheer'
print(is_anagram(word1, word2))
print(is_anagram(word3, word4))
