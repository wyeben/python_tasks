def is_anagram(s, t):
    if len(s) != len(t):
        return 'please words length is not the same'

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



