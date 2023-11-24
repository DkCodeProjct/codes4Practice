import random

def main():
    getName = input("enterPlayerName: ")
    if len(getName) >= 2 and len(getName) <= 6:
        
        getUserChoice = input("what Words You Prefer??\nsharks_/dragons ")
        
        if getUserChoice == 'sharks':
            result0 = wordShark(getUserChoice)
            print(result0)
        else:
            result1 = wordDragon(getUserChoice)
            print(result1)
    
    else:
        print("invlaid")

def wordShark(name):
    words = ["kevin", "mark", "lori", "daymond", "robert", "peter"]
    word  = random.choice(words)

    attempts0 = 5

    while attempts0 > 0:
        getUserChar = input("enterChar ")
        foundChar = False
        for char in word:
            if char in getUserChar:
                print(char,end="")
                foundChar = True
            else:
                print("_",end="")
        print()

        if set(word) == set(getUserChar):
            print("win!!")
            break
        else:
            attempts0 -= 1
    if attempts0 == 0:
        print("you've reached maximum attempts\nThe word is ", word)

def wordDragon(k):
    words = ["kevin", "arlen", "petre", "ksi"]
    word  = random.choice(words)

    attempts = 5

    while attempts > 0:
        getUserChar1 = input("enter ")
        
        foundChar = False
        for char in word:
            if char in getUserChar1:
                print(char,end="")
                foundChar = True
            else:
                print("_",end="")
        print()

        if set(word) == set(k):
            print("win!!")
            break
        else:
            attempts -= 1
    if attempts == 0:
        print("you've reached maximum attempts\nThe word is ", word)

if __name__ == "__main__":
    main()