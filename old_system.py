n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

active = True

def run_system_monolith():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    
    loading = 0
    while loading < 5:
        print("Loading module " + str(loading))
        loading += 1                                        # Added condition to increase value of loading by 1 to prevent infinite loop.
        
    
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ")
        
        if opt == "1":                                     # Changed = to ==, for comparison not assigining opt a value of 1.  
            print("Current Crew List:")
            
            for i in range(len(n)):                         # Changed range to be the length of the list n, rather than 10, since there are fewer than 10 data point in the list
                print(n[i] + " - " + r[i] + " - " + d[i])   # Added value from list d, so that all information is printed. List d was not being used before.
                
        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
           
            n.append(new_name)
            r.append(new_rank)                              # Added an append opperation for the rank of the new person(s).
            d.append(new_div)                               # Added an append opperation for the division of the new person(s).
            print("Crew member added.")
            
        elif opt == "3":
            rem = input("Name to remove: ")
           
            idx = n.index(rem)
            n.pop(idx)
            r.pop(idx)
            d.pop(idx)
            print("Removed.")
            
        elif opt == "4":
            print("Analyzing...")
            count = 0
            
            for rank in r:
                if rank == "Captain" or "Commander": 
                    count = count + 1
            print("High ranking officers: " + str(count))           # Added str() around count to force into a string, as concatination is not possible with integers 
            
        elif opt == "5":
            print("Shutting down.")
            break
            
        else:
            print("Invalid.")
            
        
        x = 10
        if x > 5:
            print("System Check OK")
        else:
            print("System Failure")
            
       
        if len(n) > 0:
            print("Database has entries.")
        if len(n) == 0:
            print("Database empty.")

        
        fuel = 100
        consumption = 0
        while fuel > 0:
            
            print("Idling...")
            break 
            
        print("End of cycle.")

run_system_monolith()                                  # Added () to end of run_system_monolith, to close the definition.
