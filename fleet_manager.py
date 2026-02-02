def init_database():

    names = ["Picard", "Riker", "Data", "Worf"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
    divs = ["Command", "Command", "Operations", "Security"]
    ids = [1, 2, 3, 4]
    return(names, ranks, divs, ids)

init_database()

def display_menu():

    name_in = input("What is your full name?")
    print("Currently logged in: " + name_in)
    print("Options: ")
    print("1. View Crew")
    print("2. Add Crew")
    print("3. Remove Crew")
    print("4. Analyze Data")
    print("6. Exit")
    option = input("Chosen Option: ")
  
    return(option)

display_menu()

def add_member(names, ranks, divs, ids):
    print("This is a placeholder")
add_member()

def remove_member(names, ranks, devs, ids):
    print("This is a placeholder")
remove_member()

def update_rank(names, ranks, ids):
    print("This is a placeholder")
update_rank()

def display_roster(names, ranks, divs, ids):
    print("This is a placeholder")
display_menu()

def search_crew(names, ranks, divs, ids):
    print("This is a placeholder")
search_crew()

def filter_by_division(names, divs):
    print("This is a placeholder")
filter_by_division()

def calculate_payroll(ranks):
    print("This is a placeholder")
calculate_payroll()

def count_officers(ranks):
    print("This is a placeholder")
count_officers()

def main():

    option = display_menu()
  
    if option == 1:
        print("1")
    elif option == 2:
        print("2")
    elif option == 3:
        print("3")
    elif option == 4:
        print("4")
    elif option == 5:
        print("5")
    elif option == 6:
        print("6")
    else:
        print("Invalid Input")

main()
