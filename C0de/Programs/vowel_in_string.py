# Check Vowel in a string(have to try using 'in' function )
s = input("Enter string :")
v = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
for i in range(len(s)):
    for j in range(10):
        if(s[i] == v[j]):
            print("Vowel : "+s[i])
