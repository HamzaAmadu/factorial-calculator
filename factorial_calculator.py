# Factorial Calculator Program

print("    Factorial Calculator   ")
print("Welcome, This program calculates the factorial of a number you put in.")
print("Example: 5! = 5 × 4 × 3 × 2 × 1 = 120")
print()

# Getting input from user
user_input = input("enter a non-negative integer: ")

# Check if input is a valid number
try:
    number = int(user_input)

    # Check if number is negative
    if number < 0:
        print("Error: Please enter a non-negative number. Negative numbers dont have factorials, Thanks.")
    else:
        # Calculate factorial
        factorial_result = 1

        # Special case: 0! = 1
        if number == 0:
            factorial_result = 1
        else:
            # Multiply all numbers from 1 to the input number
            for i in range(1, number + 1):
                factorial_result = factorial_result * i
                print(f"Step {i}: {factorial_result}")

        # Display the result
        print()
        print(f" The factorial of {number} is: {factorial_result}")
        print(f"   {number}! = {factorial_result}")

except ValueError:
    # This runs if the input cannot be converted to an integer
    print(" Error: Please enter a valid whole number thats not a non-negative number.")
