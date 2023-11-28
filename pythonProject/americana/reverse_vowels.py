def reverse_vowel(ip):
    vowels = "aeiouAEIOU"
    ip = list(ip)
    i, j = 0, len(ip) - 1

    while i < j:
        if ip[i] in vowels and ip[j] in vowels:
            ip[i], ip[j] = ip[j], ip[i]
            i += 1
            j -= 1
        elif ip[i] not in vowels:
            i += 1
        elif ip[j] not in vowels:
            j -= 1

    return ''.join(ip)


giving1 = "hEllo"
giving2 = "leetcode"
print(reverse_vowel(giving1))
print(reverse_vowel(giving2))
