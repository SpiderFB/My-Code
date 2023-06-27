def countVowels(list_name):
    vowels = ['a', 'e', 'i', 'o', 'u']  # list of vowels
    empty_dictionary = {}  # an empty dictionary
    for i in vowels:
        empty_dictionary[i] = 0
    for i in "".join(list_name):
        if i == "a" or i == "A":
            empty_dictionary['a'] += 1
        elif i == "e" or i == "E":
            empty_dictionary['e'] += 1
        elif i == "i" or i == "I":
            empty_dictionary['i'] += 1
        elif i == "o" or i == "O":
            empty_dictionary['o'] += 1
        elif i == "u" or i == "U":
            empty_dictionary['u'] += 1
    vowel_dictionary = {k: v for k, v in empty_dictionary.items() if v != 0}
    return vowel_dictionary


print(countVowels(["hello"]))
