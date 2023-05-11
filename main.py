
print("\t\t\t Welcome to Switzerland \t\t\n")
print("\t\t\t " + "~" * len("Welcome to Switzerland") + " \t\t\n")


# Define the available cantons
cantons = ["Zurich", "Berne", "Luzern", "Uri", "Schwyz", "Obwalden", "Nidwalden", "Glarus", "Zug",
           "Fribourg", "Solothurn", "Basel-Stadt", "Basel-Landschaft", "Schaffhausen", "St. Gallen", "Graubunden", "Aargau", "Thurgau", "Tessin", "Vaud", "Valais",
           "Neuchatel", "Genève", "Jura"]

        #lezem nrodou lessemi eli f graph compatible!!!
        

# Define a function to validate user input for canton selection
def validate_canton(canton):
    return canton in cantons

# Define a function to validate user input for choice selection
def validate_choice(choice):
    return choice in range(1, 6)

# Start the app menu loop
def menu():
    start = input("Please enter the starting canton: ")
    if not validate_canton(start):
        print("Invalid input. Please enter a valid canton.")
        continue

    destination = input("Please enter the destination canton: ")
    if not validate_canton(destination):
        print("Invalid input. Please enter a valid canton.")
        continue

    print("Please choose a search method:\n")
    print("Please enter the corresponding number:\n")
    print("\t1 - Dijkstra")
    print("\t2 - Bellman-Ford")
    print("\t3 - Breadth-first search")
    print("\t4 - Depth-first search")
    print("\t5 - Exit")

    choice = input("Enter your choice: ")
    if not choice.isdigit() or not validate_choice(int(choice)):
        print("Invalid input. Please enter a number between 1 and 5.")
        continue

    choice = int(choice)
    return choice, start, destination

while True:
    menu()
    

    # Process the user's choice
    if choice == 1:
        # Run Dijkstra's algorithm
        print("Running Dijkstra's algorithm...")
        RO2.dijkstra(G, start, destination)
        response = input("would you like to try another search method? \n enter y for yes and n for no: ")
        if response == "y":
            menu()
        else:
            print("Exiting the app...")
            break    

            

    elif choice == 2:
        # Run Bellman-Ford algorithm
        print("Running Bellman-Ford algorithm...")
        RO2.bellman_ford(G, start, destination)
        response = input("would you like to try another search method? \n enter y for yes and n for no: ")
        if response == "y":
            menu()
        else:
            print("Exiting the app...")
            break    

    elif choice == 3:
        # Run breadth-first search
        print("Running breadth-first search...")
        RO2.breadth_first_search(G, start, destination)
        response = input("would you like to try another search method? \n enter y for yes and n for no: ")
        if response == "y":
            menu()
        else:
            print("Exiting the app...")
            break    

    elif choice == 4:
        # Run depth-first search
        print("Running depth-first search...")
        RO2.depth_first_search(G, start, destination)
        response = input("would you like to try another search method? \n enter y for yes and n for no: ")
        if response == "y":
            menu()
        else:
            print("Exiting the app...")
            break    

    elif choice == 5:
        # Exit the app menu loop
        print("Exiting the app...")

        break
