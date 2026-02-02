def init_database():

    names = ["Picard", "Riker", "Data", "Worf"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
    divs = ["Command", "Command", "Operations", "Security"]
    ids = ["1", "2", "3", "4"]

    return(names, ranks, divs, ids)



def display_menu():

    name_in = input("What is your full name? ")
    print("Currently logged in: " + name_in)
    print("Options: ")
    print("1. View Crew")
    print("2. Add Crew")
    print("3. Remove Crew")
    print("4. Analyze Data")
    print("6. Exit")
    option = int(input("Chosen Option: "))

    return(option)



def add_member(names, ranks, divs, ids):

    new_name = input("Name: ")
    new_rank = input("Rank: ")
    new_div = input("Division: ")
    new_id = input("ID: ")
    
    for i in range(len(names)):
        if ids[i] == new_id:
            print("ID already taken.")
            return           

    names.append(new_name)
    ranks.append(new_rank)                       
    divs.append(new_div)
    ids.append(new_id)
    print("Crew member added.")

    return


def remove_member(names, ranks, divs, ids):

    remove = input("Name to remove: ")
           
    if remove in names:                                   
        idx = names.index(remove)
        names.pop(idx)
        ranks.pop(idx)
        divs.pop(idx)
        ids.pop(idx)

        print("Removed.")

    else:
        print("Name could not be found and was therefore no data was removed.")
    return(names, ranks, divs, ids)


def update_rank(names, ranks, ids):

    id_in = input("What is the ID of the character's rank you wish to update?")
    new_rank = input("What is " + names[i] + "'s new rank?")

    for i in range(len(names)):
        if i[ids] == id_in:
            i[ranks] = new_rank
        else:
            print("ID not found.")
    return


def display_roster(names, ranks, divs, ids):

    for i in range(len(names)):
        print(names[i] + " - " + ranks[i] + " - " + divs[i] + " - " + ids[i])
    return


def search_crew(names, ranks, divs, ids):
    print("This is a placeholder")


def filter_by_division(names, divs):
    print("This is a placeholder")


def calculate_payroll(ranks):
    print("This is a placeholder")


def count_officers(ranks):
    print("This is a placeholder")


def main():

    exit = False
    names, ranks, divs, ids = init_database()
    
    while exit == False:
        option = display_menu()
        
  
        if option == 1:
            display_roster(names, ranks, divs, ids)
        elif option == 2:
            add_member(names, ranks, divs, ids)
        elif option == 3:
            remove_member(names, ranks, divs, ids)
        elif option == 4:
            print("4")
        elif option == 5:
            print("5")
        elif option == 6:
            exit = True
        else:
            print("Invalid Input")

main()
