#practice using the deque structure
from collections import deque
import random

P1 = deque()
CPU = deque()

#create the deck list
def make_cards(lst):
    for i in range(4):
        for j in range(1,14):
                lst.append(j)
    return lst

#shuffle the deck before a new game
def shuffle(lst):
    return random.shuffle(lst)

if __name__ == '__main__':
    deck=[]
    make_cards(deck)
    #print(deck)
    shuffle(deck)
    #print(deck)
    for i in range(26):
         P1.appendleft(deck[i])
    for i in range(26,52):
         CPU.appendleft(deck[i])
    #print(P1)
    #print(len(P1))
    #print(CPU)
    #print(len(CPU))
    done = False
    print("Welcome to the Game of War")
    print("Press Enter to begin...")
    print("=================================================")
    
    while done == False:
        if len(P1)==0:
            print("CPU WINS!!!")
            done = True
            break
        if len(CPU)==0:
            print("PLAYER WINS!!!")
            done = True
            break
        player_draw=P1.pop()
        c_draw=CPU.pop()
        print(f"Computer Draws {c_draw}")
        print(f"Players Draws {player_draw}")
        print("=================================================")
        print()
        if c_draw == 0:
            c_draw = 14
        if player_draw == 0:
            player_draw = 14
        if c_draw>player_draw:
            print("Computer Wins This Hand :(")
            CPU.appendleft(c_draw)
            CPU.appendleft(player_draw)
            print(f"Player Score: {len(P1)}")
            print(f"CPU Score: {len(CPU)}")
        elif c_draw<player_draw:
            print("Player Wins This Hand :)")
            P1.appendleft(player_draw)
            P1.appendleft(c_draw)
            print(f"Player Score: {len(P1)}")
            print(f"CPU Score: {len(CPU)}")
        else:
            print("Its a Draw, players will regain these cards")
            print(f"Player Score: {len(P1)}")
            print(f"CPU Score: {len(CPU)}")
        print("=================================================")
        wait=input("Press Enter to Continue, Z to exit...")
        if wait == "Z":
            done = True
        elif wait == "SIM":
            while done == False:
                if len(P1)==0:
                    print("CPU WINS!!!")
                    done = True
                    break
                if len(CPU)==0:
                    print("PLAYER WINS!!!")
                    done = True
                    break
                player_draw=P1.pop()
                c_draw=CPU.pop()
                print(f"Computer Draws {c_draw}")
                print(f"Players Draws {player_draw}")
                print("=================================================")
                print()
                if c_draw == 0:
                    c_draw = 14
                if player_draw == 0:
                    player_draw = 14
                if c_draw>player_draw:
                    print("Computer Wins This Hand :(")
                    CPU.appendleft(c_draw)
                    CPU.appendleft(player_draw)
                    print(f"Player Score: {len(P1)}")
                    print(f"CPU Score: {len(CPU)}")
                elif c_draw<player_draw:
                    print("Player Wins This Hand :)")
                    P1.appendleft(player_draw)
                    P1.appendleft(c_draw)
                    print(f"Player Score: {len(P1)}")
                    print(f"CPU Score: {len(CPU)}")
                else:
                    print("Its a Draw, players wins")
                    P1.appendleft(player_draw)
                    P1.appendleft(c_draw)
                    print(f"Player Score: {len(P1)}")
                    print(f"CPU Score: {len(CPU)}")
        print("=================================================")