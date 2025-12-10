def get_positive_integer():
    while True:   # one loop controlling all repetition
        user_input = input("Please enter a positive integer: ")

        try:
            value = int(user_input)   # may raise ValueError
        except ValueError:
            print("Error: That is not a valid integer. Please try again.")
            continue   # go back to top of loop

        if value <= 0:
            print("Error: Number must be greater than 0. Please try again.")
        else:
            return value   # valid input found

# TEST THE FUNCTION HERE
print("Testing input validation function...")
result = get_positive_integer()
print("You entered:", result)
