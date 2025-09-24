

def check_even_odd(number):
    """
    Function to check if a number is even or odd.
    :param number: The number to check
    :return: A string indicating whether the number is even or odd
    """
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

if __name__ == "__main__":
    print("Even or Odd Checker!")
    
    # Get input from the user
    try:
        num = int(input("Enter an integer: "))
        # Check if the number is even or odd
        result = check_even_odd(num)
        # Display the result
        print(f"The number {num} is {result}.")
        
    except ValueError:
        print("Invalid input! Please enter an integer.")