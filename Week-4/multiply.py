# Prompt the user to enter a number
while True:
    try:
        num = int(input("Enter a number to generate its multiplication table: "))
        break  # Exit loop if input is valid
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Generate and print the multiplication table
print(f"\nMultiplication Table for {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
