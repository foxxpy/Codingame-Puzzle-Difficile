import sys
import math

def find_max_food(node):
    global lake, max_lake
    max_f1, max_f2 = 0, 0

    #Si on a déjà été sur cette case, on récupère sa valeur
    if node in max_lake.keys():
        return max_lake[node]

    if lake[node].lake1 == "E":
        max_f1 = lake[node].value
    else:
        max_f1 += lake[node].value + find_max_food(lake[node].lake1)

    if lake[node].lake2 == "E":
        max_f2 = lake[node].value
    else:
        max_f2 += lake[node].value + find_max_food(lake[node].lake2)

    #On garde seulement la valeur du chemin qui rapporte le plus de nourriture
    max_lake[node] = max(max_f1, max_f2)
    return max_lake[node]

class Food:
    def __init__(self, value, lake1, lake2):
        self.value = value
        self.lake1 = lake1
        self.lake2 = lake2

#Instanciation des variables
w, h = [int(i) for i in input().split()]
lake = dict()
max_lake = dict()

#On récupère la position de chaque node du lac et ses voisins
for i in range(h):
    for j, f in enumerate(input().split()):
        food = int(f)
        neighbor_column = str(i*w+j+1) if j < w - 1 else "E"
        neighbor_line = str(w*(i+1)+j) if i < h - 1 else "E"
        lake[str(i*w + j)] = Food(food, neighbor_line, neighbor_column)

#Fonction de récurrence qui calcule le maximum de nourriture pour chaque node entre ses deux voisins
max_food = find_max_food("0")
print(max_food)
