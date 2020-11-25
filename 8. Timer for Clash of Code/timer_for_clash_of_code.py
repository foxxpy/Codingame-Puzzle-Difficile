import sys
import math

def calculate_time(t, p):
    
    t = time_to_number(t)
    pow_2 = pow(2, (p-1))
    soustraction = int(256 /pow_2)
    timer = int(t - (256 / pow_2))

    return timer

def check_if_player_is_late(time, time_stamp):
    """"""
    
    time_stamp = time_to_number(time_stamp)
    
    #If player is late
    if time_stamp < time:
        return True
        
    else:
        return False

def fill_with_zero(nbr):
    """Fill a number with 0s in front of it and return it into str format"""
    
    if nbr > 10:
        return str(nbr)
        
    else:
        return "0"+str(nbr)

def number_to_time(nbr):
    """Convert a number time into a string mm:ss"""
    
    minute = int(nbr / 60)
    seconds = nbr%60
    if seconds < 10:
        seconds = fill_with_zero(seconds)
        
    return str(minute)+":"+str(seconds)
    

def time_to_number(time_str):
    """Convert string of time into number"""
    
    t = time_str.split(":")
    t = int(t[0])*60 + int(t[1])
    
    return t


# ---------------------------------------------------------------------------------------
#                                       MAIN PROGRAM
# ---------------------------------------------------------------------------------------

#Instanciation des variables
n = int(input())
p = 0
time = None
time_stamp_temp = 0
player_is_late = False


for i in range(n):    
    time_stamp = input()
    
    if time_stamp is not None:
        print("Time_stamp : "+time_stamp, file=sys.stderr)
        p = p + 1
        
        #If it is not the first time stamp
        if i > 0:
            player_is_late = check_if_player_is_late(time, time_stamp)
        
        #If a player is late
        if player_is_late:
            break;
        
        #If the last player came
        if p == 7:
            time = time_to_number(time_stamp)
            break
            
            
        time = calculate_time(time_stamp, p)
        print("Game starts at "+number_to_time(time)+"\n", file=sys.stderr)


if time is not None and time < 0:
    time = 0

#Affichage du résultat
if time is not None:
    print(number_to_time(time)) #answer
else:
    print("NO GAME")
