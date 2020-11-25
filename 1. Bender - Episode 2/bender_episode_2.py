import sys
import math

class Room:
    def __init__(self, money, r1, r2):
        self.money = money
        self.r1 = r1
        self.r2 = r2

def find_max_money(num):
    global rooms, rooms_max_money
    total_m1 = 0
    total_m2 = 0

    #Si on a déjà calculé le maximum qu'on pouvait obtenir pour cette salle, on renvoie ce maximum
    if num in rooms_max_money.keys():
        return rooms_max_money[num]

    #Sinon on le calcul en parcourant ses chemins
    if rooms[num].r1 == "E":
        total_m1 = rooms[num].money
    else:
        total_m1 += rooms[num].money + find_max_money(rooms[num].r1)

    if rooms[num].r2 == "E":
        total_m2 = rooms[num].money
    else:
        total_m2 += rooms[num].money + find_max_money(rooms[num].r2)
    rooms_max_money[num] = max(total_m1, total_m2)

    return rooms_max_money[num]



#Instanciation des variables
n = int(input())
rooms = dict()
rooms_max_money = dict()

#On récupère les pièces
for i in range(n):
    num, money, r1, r2 = input().split(" ")
    rooms[num] = Room(int(money), r1, r2)

total_money = find_max_money("0")

print(total_money)
