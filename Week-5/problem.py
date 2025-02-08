def calculate_rectangle_area():
    # Prompt user for length and width
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    
    # Calculate area
    area = length * width
    
    # Display result
    print(f"The area of the rectangle is: {area}")

# Run the function
calculate_rectangle_area()