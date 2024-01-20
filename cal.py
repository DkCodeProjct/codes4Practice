import random

def main():
    genNum = isValid('EnterRageToGenNum:N: ')
    ranNum = random.randint(1, genNum)
    attempts = 7

    while attempts  > 0:
        
        guesNum = isValid('GuessTheNum:X: ')
        
        if guesNum == ranNum:
            print("N==X",ranNum)
            break
        
        if guesNum > ranNum:
            print(f'N>X../ \nattemptsRemain{attempts}')
            attempts -= 1
        
        if guesNum < ranNum:
            print(f'N<X../ \nattemptsRemain{attempts}')
            attempts -= 1 
    
    if attempts == 0:
        print('attemptsOver../ TheNumWas: ',ranNum) 

def isValid(prompt):
    while True:
        
        try:
            num = int(input(prompt))
            if num > 0:
                return num
            else:
                pass
        
        except ValueError:
            pass

if __name__ == "__main__":
    main()
                


    