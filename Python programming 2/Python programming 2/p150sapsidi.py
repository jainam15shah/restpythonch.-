import random
import time
pos=0

while pos<100:
    y = random.randint(1, 6)
    print("Dice = ",y)
    pos+=y
    print("Your pos = ",pos)
    time.sleep(1)
        
    if pos>100:
        print("the player 1 is a winner ")
    
    # def snake_and_ladder(pos):

    #     snake_and_ladder={14:4,36:12,48:24,52:32,67:40,77:22,83:42,89:66,94:39,99:54}
    #     if pos in snake_and_ladder:
    #         print("oops")
    #         return snakes_and_ladders[pos]
    #     return position