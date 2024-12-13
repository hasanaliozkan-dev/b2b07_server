### DO NOT MODIFY BELOW LINES ###
import random
random.seed(42)
### DO NOT MODIFY ABOVE LINES ###


def sportCategoryAverages(durations):
    """
        Parameters:
            - durations: a dictionary of athlete durations
        Returns:
            - category_averages: a dictionary of category averages -> {'Football': 55.8054450872674, 'Basketball': 52.90643019980669, 'Sprint': 59.71299197416597, 'Tennis': 49.78061492521068}
    """
    categories = {
        "Football": ["Lionel Messi", "Kylian Mbappe", "Cristiano Ronaldo"],
        "Basketball": ["LeBron James", "Michael Jordan", "Kobe Bryant"],
        "Sprint": ["Usain Bolt", "Allyson Felix", "Mo Farah"],
        "Tennis": ["Serena Williams", "Roger Federer", "Rafael Nadal"]
    }

    # YOUR CODE GOES HERE


def athleteAverages(durations):

    """
    Parameters:
        - durations: a dictionary of athlete durations
    Returns:
        - averages: a dictionary of athlete averages -> {'Lionel Messi': 43.081762496949956, 'LeBron James': 59.641475208077146, 'Serena Williams': 29.732372851269776, 'Cristiano Ronaldo': 76.40189854185076, 'Roger Federer': 64.29460069344245, 'Usain Bolt': 83.57663814011072, 'Michael Jordan': 38.89747422252942, 'Allyson Felix': 42.403294367479454, 'Kylian Mbappe': 47.93267422300146, 'Rafael Nadal': 55.314871230919806, 'Mo Farah': 53.15904341490776, 'Kobe Bryant': 60.180341168813506}
    """
    # YOUR CODE GOES HERE



def printDurations(durations):
    """
    Parameters:
        - durations: a dictionary of athlete durations
    Returns:
        - None
    """
    for athlete in durations:
        print(athlete + ":")
        counter = 0
        for duration in durations[athlete]:
            counter += 1
            if counter % 7 == 0:
                print("{:.2f}".format(duration))
            else:
                print("{:.2f}".format(duration), end=" ")
        print("\n")


### DO NOT MODIFY BELOW LINES ###
durations = {
    "Lionel Messi": [random.uniform(30, 60) for i in range(31)],
    "LeBron James": [random.uniform(45, 75) for i in range(31)],
    "Serena Williams": [random.uniform(20, 40) for i in range(31)],
    "Cristiano Ronaldo": [random.uniform(60, 90) for i in range(31)],
    "Roger Federer": [random.uniform(50, 80) for i in range(31)],
    "Usain Bolt": [random.uniform(70, 100) for i in range(31)],
    "Michael Jordan": [random.uniform(25, 50) for i in range(31)],
    "Allyson Felix": [random.uniform(30, 55) for i in range(31)],
    "Kylian Mbappe": [random.uniform(35, 60) for i in range(31)],
    "Rafael Nadal": [random.uniform(40, 70) for i in range(31)],
    "Mo Farah": [random.uniform(35, 65) for i in range(31)],
    "Kobe Bryant": [random.uniform(45, 75) for i in range(31)],
}

command = input("Please enter a command: ")
while command != "quit":
    if command == "print":
        printDurations(durations)
    elif command == "athletes":
        print(athleteAverages(durations))
    elif command == "category":
        print(sportCategoryAverages(durations))
    else: 
        print("Invalid command")
    command = input("Please enter a command: ")

### DO NOT MODIFY ABOVE LINES ###