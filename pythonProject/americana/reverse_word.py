def reverse_word(a):
    words = a.split()
    reverse = [r[::-1] for r in words]
    result = ' '.join(reverse)
    return result


word = 'A better place'
word2 = "switch off moyin's phone"
print(reverse_word(word))
print(reverse_word(word2))
