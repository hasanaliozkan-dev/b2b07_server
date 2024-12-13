### DO NOT MODIFY BELOW LINES ###
import random
random.seed(42)
### DO NOT MODIFY ABOVE LINES ###


def regionCategoryAverages(sales):
    
    """
    Parameters:
        - sales: a dictionary of sales data
    Returns:
        - region_averages: a dictionary of region averages -> {'North': 1949.2903817880726, 'South': 2355.0958445288347, 'East': 2115.678267052701, 'West': 2301.6890868434166}
    """
    
    regions = {
        "North": ["Electronics", "Clothing", "Groceries"],
        "South": ["Furniture", "Books", "Toys"],
        "East": ["Sports", "Health", "Automotive"],
        "West": ["Beauty", "Jewelry", "Office Supplies"]
    }

    # YOUR CODE GOES HERE

def categoryAverages(sales):
    
    """
    Parameters:
        - sales: a dictionary of sales data
    Returns:
        - averages: a dictionary of category averages -> {'Electronics': 2744.2349995933278, 'Clothing': 1873.7081819256578, 'Groceries': 1229.9279638452333, 'Furniture': 4733.649756975127, 'Books': 871.784027737698, 'Toys': 1459.8537488736781, 'Sports': 2345.3373191430596, 'Health': 1094.5844845788495, 'Automotive': 2907.1129974361934, 'Beauty': 1520.9914153946538, 'Jewelry': 4223.856512236163, 'Office Supplies': 1160.219332899432}
    """
    
    # YOUR CODE GOES HERE


def printSales(sales):
    
    """
    Parameters:
        - sales: a dictionary of sales data
    Returns:
        - None
    Prints the sales data in a readable format
    """

    for category in sales:
        print(category + ":")
        counter = 0
        for amount in sales[category]:
            counter += 1
            if counter % 7 == 0:
                print("{:.2f}".format(amount))
            else:
                print("{:.2f}".format(amount), end=" ")
        print("\n")



### DO NOT MODIFY BELOW LINES ###
sales = {
    "Electronics": [random.uniform(1000, 5000) for i in range(31)],
    "Clothing": [random.uniform(800, 3000) for i in range(31)],
    "Groceries": [random.uniform(500, 2000) for i in range(31)],
    "Furniture": [random.uniform(2000, 7000) for i in range(31)],
    "Books": [random.uniform(300, 1500) for i in range(31)],
    "Toys": [random.uniform(600, 2500) for i in range(31)],
    "Sports": [random.uniform(900, 3500) for i in range(31)],
    "Health": [random.uniform(400, 1800) for i in range(31)],
    "Automotive": [random.uniform(1200, 4500) for i in range(31)],
    "Beauty": [random.uniform(500, 2500) for i in range(31)],
    "Jewelry": [random.uniform(1500, 6000) for i in range(31)],
    "Office Supplies": [random.uniform(300, 2000) for i in range(31)],
}


command = input("Please enter a command: ")

while command != "quit":
    if command == "print":
        printSales(sales)
    elif command == "category":
        print(categoryAverages(sales))
    elif command == "region":
        print(regionCategoryAverages(sales))
    else:
        print("Invalid command")
    command = input("Please enter a command: ")


### DO NOT MODIFY ABOVE LINES ###
