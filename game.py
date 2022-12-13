from random import randint

rounds = int(input("Enter No. of round you want to play"))
player = 0
bot = 0
d = {
    "rock" : 1,
    "paper" : 2,
    "scissor":3
}

for i in range(rounds):
    print(f"***********  ROUND {i+1} of {rounds}  ***********")
    while True:
        ch = input("Choose rock/paper/scissor >>> ").lower()
        if ch in d:
            break
        else:
            print("Please choose valid option")
        

    btch = randint(1,3)
    print(f"You choose {ch} bot choose {list(d.keys())[btch-1]}")
    if d[ch] == btch:
        print("Draw")
        player+=1
    elif d[ch] == 1 and btch == 2:
        print("You LOSS This Round")
    elif d[ch] == 1 and btch == 3:
        print("You WON This Round")
        player+=1
    elif d[ch] == 2 and btch == 1:
        print("You WON This Round")
        player+=1
    elif d[ch] == 2 and btch == 1:
        print("You LOSS This Round")
    elif d[ch] == 3 and btch == 1:
        print("You LOSS This Round")
    elif d[ch] == 3 and btch == 2:
        print("You WON This Round")
        player+=1

print(f"Score is : {player} / {rounds}")