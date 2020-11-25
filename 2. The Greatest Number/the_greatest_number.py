import sys
import math

#Instanciation des variables
n = int(input())
_input = input().split(" ")
greatest = ""
point_in_input = True if "." in _input else False
negative_number = True if "-" in _input else False


if point_in_input:
    _input.remove(".")

#Si il y'a un "-" dans l'input, le chiffre sera négatif
if negative_number:
    _input.remove("-")
    greatest += "-"
    _input = sorted(_input)

    #On ajoute les nombres triés par ordre croissant un à un et on met un point à l'incide 1
    #Si il y'avait un point dans les inputs
    for i, number in enumerate(_input):
        if i == 1 and point_in_input:
            greatest += "."
        greatest += number

    #Si il n'y a que des zéros après la virgule, on les supprime
    if point_in_input and greatest[3:].count("0") == len(greatest[3:]):
        #Si c'est un 0 on enlève le -
        if greatest[1] == "0":
            greatest = greatest[1]
        #Si c'est un chiffre, on garde le chiffre avec le moins : -9
        else:
            greatest = greatest[0:2]

#Si c'est un nombre positif
else:
    _input = sorted(_input, reverse=True)
    for i, number in enumerate(_input):
        if i == len(_input) - 1 and point_in_input:
            greatest += "."
        greatest += number
    #Si le nombre finit par ".0", on retire le ".0"
    if point_in_input and greatest[-1] == "0":
        greatest = greatest[0:len(greatest)-2]

#Résultat final
print(greatest)
