class Passenger:
    def __init__(self):
        # Define an empty list to hold passenger ages
        self.passenger_ages = []

    def menu(self):
        # Menu loop: keeps running until the user chooses to exit
        while True:
            print("\nChoose an option:")
            print("1 - List all passengers and their ages")
            print("2 - Add passenger age")
            print("3 - Calculate average age")
            print("4 - Sort passengers by age")
            print("5 - Exit the program")

            # Get user's choice
            choice = input("Enter your choice (1-5): ")

            # Call a function based on user choice
            if choice == "1":
                self.list_passengers()
            elif choice == "2":
                self.add_passenger()
            elif choice == "3":
                self.average_age()
            elif choice == "4":
                self.sort_passengers()
            elif choice == "5":
                # Exit the loop and end the program
                print("Exiting the program. Goodbye!")
                break
            else:
                # Handle invalid input
                print("Invalid choice. Please try again.")

    # Function to add a passenger age
    def add_passenger(self):
        try:
            # Ask for the passenger's age and convert to integer
            age = int(input("Enter passenger age: "))
            # Add the age to the list
            self.passenger_ages.append(age)
            print(f"{age} year old passenger added successfully.")
        except:
            # This runs when a non-integer is entered
            print("Error: Please enter a valid number. (Whole Number)")

    # Function  to list all passengers and their ages
    def list_passengers(self):
        print("\nAll passengers:")
        # Check if the list is empty
        if not self.passenger_ages:
            print("No passengers have been added yet.")
        else:
            print("Passengers and their ages:")
            # Loop through the list and print each passenger's age
            for i, age in enumerate(self.passenger_ages, 1):
                print(f"{i}. Passenger: {age} years old")

    # Function to calculate and print the average age
    def average_age(self):
        if not self.passenger_ages:
            print("No passengers have been added yet.")
            return
        total = 0
        # Go through each age and add it to the total
        for age in self.passenger_ages:
            total += age
        # Calculate average
        average = total / len(self.passenger_ages)
        print("\nAverage age is:", average)
        

    # This sorts the passenger ages starting with the youngest
    def sort_passengers(self):
        # Check if the list is empty
        if not self.passenger_ages:
            print("No passengers have been added yet.")
        else:
            # Sort the list
            self.passenger_ages.sort()
            print("Passengers are sorted by age:")
            # Use the same method to show the sorted list of passengers
            self.list_passengers()

# Start program
# Create the bus system so we can add passengers and run the menu.
buss = Passenger()
# Start the menu loop
buss.menu()
