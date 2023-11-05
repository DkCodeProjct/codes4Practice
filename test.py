def guess_what_x():
    attempts = 0
    while attempts < 3:
        
        user_input = input("x + 2 * 2 + 3 == 11\nWhat's X (math expression): ")
        try:
            if eval(user_input) == 2:
                return True
            else:
                print(f"The equation {user_input} does not equal 11. Try again.")

        except:
            print("Invalid input. Please enter a valid math expression.")
        attempts += 1
    return False

success = guess_what_x()
if success:
    print("Congratulations, you guessed correctly!")

else:
    print("You've reached the maximum number of attempts.")
