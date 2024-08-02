import random
print("\t\tNumber Guessing Game")
print("I'm thinking of a number between 1 and 100")
difficulty=input("Choose a difficulty(easy or hard): ").lower()
if difficulty=="easy":
    n=10
else:
    n=5
number=random.randint(1,100)
f=0
for i in range(n,0,-1):
    print("You have",i,"attempts remaining to guess the number")
    x=int(input("Make a guess: "))
    if x==number:
        print("You got it! The answer was",x)
        f=1
        break
    elif x<number:
        print("Too low")
    elif x>number:
        print("Too high")
    if i>1:
        print("Guess again")
if f==0:
    print("You've run out of guesses, you lose")

