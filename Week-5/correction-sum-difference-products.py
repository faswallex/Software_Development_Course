def basic_arithmetic_operations():
    # Prompt user for two numbers
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    
    # Validate input
    try:
        if '.' in num1 or '.' in num2:
            num1, num2 = float(num1), float(num2)
            is_float = True
        else:
            num1, num2 = int(num1), int(num2)
            is_float = False
    except ValueError:
        print("Invalid input")
        return
    
    # Perform calculations
    sum_result = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    quotient = num1 / num2 if num2 != 0 else "Undefined (division by zero)"
    
    # Ensure the result type
    if not is_float:
        sum_result = int(sum_result)
        difference = int(difference)
        product = int(product)
        quotient = int(quotient) if num2 != 0 else quotient
    
    # Display results
    print(f"Sum: {sum_result}")
    print(f"Difference: {difference}")
    print(f"Product: {product}")
    print(f"Quotient: {quotient}")

# Run the function
basic_arithmetic_operations()
