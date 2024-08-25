import random
scretnum=random.randint(1,20)
   
print(scretnum)
count=0
while(True):
    guess=int(input("Guess the number>> "))
    if guess==scretnum:
        print("YOU WON!")
        break
    
    else:
        print("You lost! Try Again")
        count+=1
        print(f"you took {count} chances")
      