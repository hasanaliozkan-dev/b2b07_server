### DO NOT MODIFY BELOW LINES ###
import random
random.seed(42)
### DO NOT MODIFY ABOVE LINES ###


def categoryAverages(fuel_usages):
    """
    Parameters:
        - fuel_usages: a dictionary of fuel usages
    Returns:
        - category_averages: a dictionary of category averages -> {'Compact': 7.453412863863124, 'SUV': 9.919012058893355, 'Sport': 10.470986810769269, 'Luxury': 13.560317290498846}
    """
    categories = {
        "Compact": ["Nissan", "Toyota", "Ford"],
        "SUV": ["Chevrolet", "Volvo", "Volkswagen"],
        "Sport": ["BMW", "Honda", "Audi"],
        "Luxury": ["Mercedes-Benz", "Bentley","Porche"]
    }

    # YOUR CODE GOES HERE


def brandAverages(fuel_usages):
    """
    Parameters:
        - fuel_usages: a dictionary of fuel usages
    Returns:
        - averages: a dictionary of brand averages -> {'Toyota': 5.872117499796664, 'Ford': 6.976098347205144, 'Honda': 5.473237285126977, 'Chevrolet': 11.093459902790052, 'Volvo': 9.95297337956283, 'BMW': 11.905109209340713, 'Bentley': 16.66769690670353, 'Mercedes-Benz': 14.992263549398356, 'Audi': 14.034613937840117, 'Porche': 9.020991415394652, 'Volkswagen': 8.710602894327183, 'Nissan': 9.512022744587567}
    """
    # YOUR CODE GOES HERE




def printFuelUsages(fuel_usages):
    """
    Parameters:
        - fuel_usages: a dictionary of fuel usages
    Returns:
        - None
    """
    for brand in fuel_usages:
        print(brand + ":")
        counter = 0
        for usage in fuel_usages[brand]:
            counter += 1
            if counter % 7 == 0:
                print(usage)
            else:
                print(usage, end=" ")
        print("\n")


### DO NOT MODIFY BELOW LINES ###
fuel_usages = {
    "Toyota": [random.uniform(5.0, 7.0) for i in range(31)],
    "Ford": [random.uniform(6.0, 8.0) for i in range(31)],
    "Honda": [random.uniform(4.5, 6.5) for i in range(31)],
    "Chevrolet": [random.uniform(10.0, 12.0) for i in range(31)],
    "Volvo": [random.uniform(9.0, 11.0) for i in range(31)],
    "BMW": [random.uniform(11.0, 13.0) for i in range(31)],
    "Bentley": [random.uniform(15.0, 18.0) for i in range(31)],
    "Mercedes-Benz": [random.uniform(14.0, 16.0) for i in range(31)],
    "Audi": [random.uniform(13.0, 15.0) for i in range(31)],
    "Porsche": [random.uniform(8.0, 10.0) for i in range(31)],
    "Volkswagen": [random.uniform(7.5, 9.5) for i in range(31)],
    "Nissan": [random.uniform(8.5, 10.5) for i in range(31)],
}

command = input("Please enter a command: ")

while command != "quit":
    if command == "print":
        printFuelUsages(fuel_usages)
    elif command == "brand":
        print(brandAverages(fuel_usages))
    elif command == "category":
        print(categoryAverages(fuel_usages))
    else: 
        print("Invalid command")
    command = input("Please enter a command: ")


### DO NOT MODIFY ABOVE LINES ###