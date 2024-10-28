def calculate_average(numbers):
    
    try:
        total = sum(numbers)
        count = len(numbers)
        if count == 0:
            return 0  
        return total / count
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return 0

def get_valid_number(prompt):
    
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    
    print("Welcome to the Average Calculator!")
    
    numbers = []
    for i in range(3):
        number = get_valid_number("Enter number " + str(i + 1) + ": ")
        numbers.append(number)
    
    average = calculate_average(numbers)
    print("The average of the numbers is: {:.2f}".format(average))

if __name__ == "__main__":
    main()