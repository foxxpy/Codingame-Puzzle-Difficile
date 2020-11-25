import sys
import math

#Instanciation des variables
n = int(input())
t = int(input())
even = True if n % 2 == 0 else False
left_tower = [x for x in range(n, 0, -1)]
towers = [left_tower, [], []]
print("n : "+str(n), file=sys.stderr)
print("t : "+str(t), file=sys.stderr)

def display_towers(towers, n):
    display = []
    #On place les tours
    for i in range(n):
        line = n*" "+"|"+(2*n+1)*" "+"|"+(2*n+1)*" "+"|"
        display.append(line)

    #On place les disques
    for i, tower in enumerate(towers):
        for j, disk in enumerate(tower):
            num_line = len(display) - j - 1
            k = 0
            if i == 0:
                k = n
            elif i == 1:
                k = 3*n + 2
            else:
                k = 5*n + 4
            display[num_line] = display[num_line][:k-disk]+"#"*(disk*2+1)+display[num_line][k+disk+1:]

    for line in display:
        print(line)

def valid_tower(k, disk, even):
    global towers
    tower_valid = False

    while(not tower_valid):
        k = 0 if k == 3 else k
        k = 2 if k < 0 else k
        print("k : "+str(k), file=sys.stderr)
        if (len(towers[k]) > 0 and towers[k][-1] > disk) or len(towers[k]) == 0:
            tower_valid = True
        else:
            if disk == 1 and even or disk > 2:
                k = k + 1
            else:
                k = k - 1

    return k

def move_disk(disk, positions_disks, even):
    
    pos_disk = positions_disks[disk]
    if even and disk == 1 or disk > 1:
        new_pos_disk = valid_tower(pos_disk+1, disk, even)
    else:
        new_pos_disk = valid_tower(pos_disk-1, disk, even)
        
    return new_pos_disk

#On stocke la position de chaque disque dans un dictionnaire
#Au tout début, tous les disques sont sur la tour 0 (celle à gauche)
position_disks = {}
for i in range(1, n+1):
    position_disks[i] = 0

#On calcule le mouvement des disques à chaque tour
for i in range(1, t+1):
    new_pos_disk = int()
    disk_moving = 0

    if i % 2 == 1:
        new_pos_disk = move_disk(1, position_disks, even)
        disk_moving = 1

    else:
        #On cherche quel disque déplacer par rapport aux puissances de 2
        for j in range(n-1, 0, -1):
            if i % (2**j) == 0:
                disk_moving = j+1
                new_pos_disk = move_disk(j+1, position_disks, even)
                break

    towers[position_disks[disk_moving]].remove(disk_moving)
    towers[new_pos_disk].append(disk_moving)


#On affiche l'état du jeu ) l'instant t
display_towers(towers, n)

#On affiche le nombre total de coups à effectuer pour résoudre la tour de hanoi
print(2**n - 1)
