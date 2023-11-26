import  random

num = int(input("enter Level ")) 
randomNum = random.randint(1,num)
while True:
    getGuss = int(input("gues num "))

    if getGuss > randomNum:
        print("too larg")
    elif getGuss < randomNum:
        print("too small ")
    elif getGuss == randomNum:
        print("just right", randomNum)
        break
    else:
        print("invalid")

        
    
