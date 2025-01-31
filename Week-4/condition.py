while True:
    try:
        age = int(input("Enter your age: "))  # Get user input and convert to integer
        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
        else:
            break  # Exit loop if valid input is provided
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Determine if the user is an adult or a minor
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
