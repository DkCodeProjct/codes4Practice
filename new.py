acceptedCoin = [10, 20, 5, 30]
cockPrice = 50
pay = 0

while pay < cockPrice:
    getCoin = int(input("enter [$10, $20, $5, $30] "))
    if getCoin in acceptedCoin:
        pay += getCoin
        print(f"ammount deu: {cockPrice - pay}")
        
    else:
        print("invlaid")
        break
        
if pay >= cockPrice:
    change = pay - cockPrice 
    print(f"change: {change}")
