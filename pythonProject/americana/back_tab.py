def can_transform(word1, word2):
    while '##' in word1:
        word1 = word1.replace('##', '')

    word1 = word1.replace('#', '')
    word2 = word2.replace('#', '')

    return word1 == word2


word1 = 'a#b#d#pqrs#'
word2 = 'ac#d##pqr'

result = can_transform(word1, word2)
print(result)
