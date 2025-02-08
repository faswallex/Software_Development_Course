def basic_arithmetic_operations():
    # Prompt user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Perform calculations
    sum_result = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    quotient = num1 / num2 if num2 != 0 else "Undefined (division by zero)"
    
    # Display results
    print(f"Sum: {sum_result}")
    print(f"Difference: {difference}")
    print(f"Product: {product}")
    print(f"Quotient: {quotient}")

# Run the function
basic_arithmetic_operations()