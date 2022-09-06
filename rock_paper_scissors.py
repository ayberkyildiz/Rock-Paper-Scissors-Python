import random

pc= random.randint(1,3)

#rock=1
#paper=2
#scissors=3

def game():
    
    chs= str(input("Choose one of rock, paper or scissors!: "))
    
    
    if chs==("rock"):
        print("You picked rock!")
    
        if pc==1:
            print("Computer picked rock!")
            print("That is a tie!")
        if pc==2:
            print("Computer picked paper!")
            print("You lost:(")
        if pc==3:
            print("Computer picked scissors!")
            print("You won:)")
        
     
    elif chs==("paper"):
        print("You picked paper!")
    
        if pc==1:
            print("Computer picked rock!")
            print("You won:)")
        if pc==2:
            print("Computer picked paper!")
            print("That is a tie!")
        if pc==3:
            print("Computer picked scissors!")
            print("You lost:(")
    
    elif chs==("scissors"):
        print("You picked scissors!")
    
        if pc==1:
            print("Computer picked rock!")
            print("You lost:(")
        if pc==2:
            print("Computer picked paper!")
            print("You won:)")
        if pc==3:
            print("Computer picked scissors!")
            print("That is a tie!")
    
    else:
        print("Invalid input!")
    
    
    
game()                  
    
