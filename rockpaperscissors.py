import random
mymove = input("enter your move (rock,paper or scissors): ")
mylist = ['rock', "paper", "scissors"]
computermove = random.choice(mylist)
print(computermove)
# score = 0

def who_won(c1,c2):

    if c1 == c2:
        return "it is a draw!", 0
    elif c1 == 'rock'and c2 == 'paper':   
        return "you have lost!",  1 
    elif c1 =='rock' and c2 == "scissors":
        return "congrats! you won! ", -1 
    elif c1 == "paper" and c2 == "rock":
        return "congrats! you won! ", -1 
    elif c1 == "paper" and c2 == "scissors":
        return  "you have lost!", +1
    elif c1 == "scissors" and c2 == "rock":
        return "you have lost! ",  + 1  
    elif c1 == "scissors" and c2 == "paper":
        return "you have won! scissors cut paper",-1  
  
# msg, result = who_won(mymove,computermove)  
 
yourscore = 0
computerscore = 0
while not yourscore == 3 and not computerscore == 3:
    mymove = input("enter your move:")
    computermove = random.choice(mylist)
    msg, result = who_won(mymove,computermove)   
    if result == -1 :
        yourscore = yourscore + 1
    elif result == 1:
        computerscore = computerscore + 1
    print(computermove)
    print("yourscore: ", yourscore, "computerscore: " , computerscore)




# while score == 3:
#     msg, computerscore = who_won()
#     score += computerscore
#     print(who_won(mymove,computermove))