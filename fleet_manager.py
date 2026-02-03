def init_database():

    names = ["Picard", "Riker", "Data", "Worf"]
    ranks = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant"]
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
    print("4. Update Crew Member Rank.")
    print("5. Search Database")
    print("6. Filter by Division.")
    print("7. Display number of Officers")
    print("8. Calculate Payroll.")
    print("9. Exit")
    option = int(input("Chosen Option: "))

    return(option)


def add_member(names, ranks, divs, ids):

    new_name = input("Name: ")
    new_rank = input("Rank: ")
    new_div = input("Division: ")
    new_id = input("ID: ")
    
    for i in range(len(names)):
        if new_rank != "Admiral V" and new_rank != "Admiral IV" and new_rank != "Admiral III" and new_rank != "Admiral II" and new_rank != "Admiral I" and new_rank != "Captain" and new_rank != "Commander" and new_rank != "Lieutenant Commander" and new_rank != "Lieutenant" and new_rank != "Lieutenant Junior Grade" and new_rank != "Ensign" and new_rank != "Petty Officer":
            print("Not an accepted rank.")
            return
        
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

    remove = input("ID to remove: ")
           
    if remove in ids:                                   
        idx = ids.index(remove)

        print(names[idx] + " Removed.")

        names.pop(idx)
        ranks.pop(idx)
        divs.pop(idx)
        ids.pop(idx)

    else:
        print("Name could not be found, therefore no data was removed.")
    return


def update_rank(names, ranks, ids):

    id_in = input("What is the ID of the character's rank you wish to update?")

    if id_in not in ids:
        print("No ID found.")
        return

    for i in range(len(ids)):
        if ids[i] == id_in:
            id_name = names[i]

    print(id_name + " is currently a " + ranks[i])
    new_rank = input("What is " + id_name + "'s new rank? ")
    
    ranks[i] = new_rank

    print(id_name + "'s Rank Updated.")
    return


def display_roster(names, ranks, divs, ids):

    for i in range(len(names)):
        print(names[i] + " - " + ranks[i] + " - " + divs[i] + " - " + ids[i])
    return


def search_crew(names, ranks, divs, ids):
    term = input("What term do you want to search for? ")
    for i in range(len(names)):
        if (term.lower()) in (names[i].lower()):
            print(names[i] + " - " + ranks[i] + " - " + divs[i] + " - " + ids[i])
        


def filter_by_division(names, divs):
    print("Which divisions do you want to filter by?")
    division_in = input("Command, Opperations or Sciences? ")
    
    for i in range(len(divs)):
        if divs[i] == division_in:
            print(names[i])


def calculate_payroll(ranks):
    pay = 0
    for i in range(len(ranks)):
        if ranks[i] == "Petty Officer":
            pay =+ 100
        elif ranks[i] == "Ensign":
            pay =+ 200
        elif ranks[i] == "Lieutenant Junior Grade":
            pay =+ 300
        elif ranks[i] == "Lieutenant":
            pay =+ 400
        elif ranks[i] == "Lieutenant Commander":
            pay =+ 500
        elif ranks[i] == "Commander":
            pay += 750
        elif ranks[i] == "Captain":
            pay =+ 1000
        elif ranks[i] == "Admiral I":
            pay =+ 1250
        elif ranks[i] == "Admiral II":
            pay =+ 1500
        elif ranks[i] == "Admiral III":
            pay =+ 2000
        elif ranks[i] == "Admiral IV":
            pay =+ 3000
        elif ranks[i] == "Admiral V":
            pay =+ 4000
    print("The paycheck for this ship is £" + str(pay))

def count_officers(ranks):
    
    count = 0
    for i in range(len(ranks)):
        if ranks[i] == "Captain" or ranks[i] == "Commander":
            count += 1
    return(count)


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
            update_rank(names, ranks, ids)
        elif option == 5:
            search_crew(names, ranks, divs, ids)
        elif option == 6:
            filter_by_division(names, divs)
        elif option == 7:
            print(str(count_officers(ranks)) + " officers in database.")
        elif option == 8:
            calculate_payroll(ranks)
        elif option == 9:
            exit = True
            print("Exiting...")
        else:
            print("Invalid Input")

main()  # I have no clue about Star Trek lore, so dont be suprised if I have missed some ranks.
