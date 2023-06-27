f1 = input('Enter file name : ')
word1 = input('Enter old string : ')
word2 = input('Enter new string : ')
f3 = []
with open(f1, 'r') as f2:
    for i in f2:
        f3.append(i.replace(word1, word2))
f2.close()
with open(f1, 'w') as f2:
    f2.write(''.join([str(item) for item in f3]))
f2.close()
