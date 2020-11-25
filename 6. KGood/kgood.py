import sys
import math

#Instanciation des variables
s = input()
k = int(input())
max_letters = 0

for i in range(len(s)):
    j = i
    letters = []
    #Tant qu'on a pas rencontré k lettres différentes ou qu'on a k lettres différentes mais que la lettre
    #à la position j est dans les lettres que l'on a rencontré jusque là
    while(j < len(s) and (len(letters) < k or len(letters) == k and s[j] in letters)):
        if not s[j] in letters:
            letters.append(s[j])
        j = j + 1

    if j - i - 1 > max_letters:
        max_letters = j - i

print(max_letters)
