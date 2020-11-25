import sys
import math

def walk(position, total_food = 0):
    global foods, h, w, max_food
    line = position[0]
    col = position[1]
    nb_path = 0

    #Si on sort du labyrinth on renvoie 0
    if line > h - 1 or col > w - 1:
        return 0

    else:
        total_food += foods[line][col]

    #Si on a atteint l'arrivée on renvoie 1
    if line == h - 1 and col == w - 1:
        if total_food > max_food:
            max_food = total_food
        return 0

    #Sinon on teste d'aller sur la case à droite et la case en dessous
    else:
        walk((line+1,col), total_food)
        walk((line, col+1), total_food)

#Instanciation des variables
w, h = [int(i) for i in input().split()]
foods = []
max_food = 0

#On récupère la grille avec la nourriture
for i in range(h):
    line_food = []
    for j in input().split():
        food = int(j)
        line_food.append(food)
    foods.append(line_food)

walk((0,0))

print(max_food)