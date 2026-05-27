#2. The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.
import random
def game():
    print("you are playing the game")
    score=random.randint(1,10)
    with open("highscore.txt","r") as f:
        hiscore=f.read()
        if(hiscore!=""):
            highscore=int(hiscore)
        else:
            highscore=0
    print(f"your score is {score}")
    if(score>highscore):
        with open("highscore.txt","w") as f:
            f.write(str(score))
    return score

game()



