def number_of_vowels(word):
    vowels = "aeiouAEIOU"
    vow_col = 0
    for letter in word:
        if letter in vowels:
            vow_col += 1
    return vow_col
