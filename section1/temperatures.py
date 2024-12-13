### DO NOT MODIFY BELOW LINES ###
import random
random.seed(42)
### DO NOT MODIFY ABOVE LINES ###

def seasonalAverages(temperatures):
    """
    Parameters:
        - temperatures: a dictionary of monthly temperatures
    Returns:
        - seasonal_averages: a dictionary of seasonal averages -> {'Winter': 2.0, 'Spring': 17.054347826086957, 'Summer': 34.78260869565217, 'Autumn': 19.65934065934066}
    """
    seasons = {
        "Winter": ["December", "January", "February"],
        "Spring": ["March", "April", "May"],
        "Summer": ["June", "July", "August"],
        "Autumn": ["September", "October", "November"]
    }

    # YOUR CODE GOES HERE

def monthlyAverages(temperatures):
    """
    Parameters:
        - temperatures: a dictionary of monthly temperatures
    Returns:
        - averages: a dictionary of monthly averages -> {'January': 1.3870967741935485, 'February': 4.535714285714286, 'March': 12.838709677419354, 'April': 17.766666666666666, 'May': 20.580645161290324, 'June': 30.366666666666667, 'July': 36.25806451612903, 'August': 37.58064516129032, 'September': 29.133333333333333, 'October': 19.580645161290324, 'November': 10.266666666666667, 'December': 0.3225806451612903}
    """

    # YOUR CODE GOES HERE



def printTemperatures(temperatures):
    """
    Parameters:
        - temperatures: a dictionary of monthly temperatures
    Returns:
        - None
    Prints the temperatures in a readable format
    """

    for month in temperatures:
        print(month + ":")
        counter = 0
        for temp in temperatures[month]:
            counter += 1
            if counter % 7 == 0:
                print(temp)
            else:
                print(temp, end = " ")
        print("\n")

### DO NOT MODIFY BELOW LINES ###

temperatures = {
    "January": [random.randint(-2, 6) for i in range(31)],
    "February": [random.randint(0, 10) for i in range(28)],
    "March": [random.randint(10, 15) for i in range(31)],
    "April": [random.randint(12, 23) for i in range(30)],
    "May": [random.randint(15, 25) for i in range(31)],
    "June": [random.randint(26, 35) for i in range(30)],
    "July": [random.randint(32, 40) for i in range(31)],
    "August": [random.randint(34, 42) for i in range(31)],
    "September": [random.randint(25, 35) for i in range(30)],
    "October": [random.randint(15, 25) for i in range(31)],
    "November": [random.randint(5, 15) for i in range(30)],
    "December": [random.randint(-5, 5) for i in range(31)],
}

command = input("Enter a command: ")

while command != "quit":
    if command == "seasonal":
        print(seasonalAverages(temperatures))
    elif command == "monthly":
        print(monthlyAverages(temperatures))
    elif command == "print":
        printTemperatures(temperatures)
    else:
        print("Invalid command.")
    command = input("Enter a command: ")
    
### DO NOT MODIFY ABOVE LINES ###





