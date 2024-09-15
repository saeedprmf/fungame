import time
import keyboard
import os
import random
objects = {
    0:".",
    1:"▲",
    2:"!",
    3:"@"
    
}



def get_int():
    try:
        n = int(input())
        return n
    except:
        print("enter jost a number")
        return get_int()

def make_map(w,h):
    _map = [[0 for i in range(w)] for j in range(h)]
    return _map

def draw(_map):
    os.system("cls")
    for j in _map:
        for i in j:
            print(objects[i],end="") 
        print("")

def move(player):
    if keyboard.is_pressed("d"):
        player[1] += 1
    elif keyboard.is_pressed("a"):
        player[1] -= 1

def shoot(player):
    global bullets
    bullets.append([-2,player[1]])


def enemy_attac():
    global enemies
    p = random.randint(0,101)
    if p >10:
        enemies[random.randint(0,len(enemies)-1)][3] = 1
        

def main_loop(enemies):
    global W,H,player,bullets
    _map = make_map(W,H)
    last_move = 0
    last_shoot = 0
    last_a = 0
    last_em = 0
    status = 0
    game = True
    while game:
        _map = make_map(W,H)
        now = time.time()
        if (now-last_move) > .1:
            move(player)
            las_move = now
            
        if (now-last_shoot) > 1:
            shoot(player)
            last_shoot = now

        _map = make_map(W,H)
        _map[-1][player[1]%W] = 1
        for b in bullets:
            _map[b[0]][b[1]%W] = 2
            b[0] -= 1
            if b[0] < H * -1:
                bullets.remove(b)
            for e in enemies:
                if e[0]<H-1:
                    if e[0] == (b[0] + H) and e[1] == b[1]%W and e[2] >-1:
                        bullets.remove(b)
                        e[2] -= 1    
                else:
                    status -= 1
                    game = False  
        point = 0    
        for e in enemies:
            if e[2] > 0:
                _map[e[0]][e[1]%W] = 3
            else:
                point += 1
        if (now-last_em) > .5:
            for e in enemies:
                    if e[3] == 1 and e[2] > 0:
                        e[0]+=1   
            last_em = now                 
        draw(_map)
        if len(enemies)>0 and (now-last_a)>6:
            last_a = now
            enemy_attac()
        
        if point >= W:
            game = False
            status +=1
    if  status == 1:
        print("you won")
    else:
        print("game over")
    
def main():
    global W,H,player,bullets,enemies
    print("enter width of map:")
    W = get_int()
    print("enter hight of map:")
    H = get_int()    
    bullets = []
    player = [-1,int(W/2)]
    enemies = [[1,i,3,0] for i in range(W)]
    main_loop(enemies)
    
    
main()

input()
