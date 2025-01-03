def adding_report(report = ""): 
    name = input("Please provide your full name: ")
    total= 0
    items = "Items\n"

    while True:
            userinp= input("Enter a integer or \"Q\" to quit: ")
            if report.upper() == 'T':
                if userinp.isdigit():
                    total = int(userinp) + total 
                    items = items + userinp + "\n"
                    print(total)
                elif userinp.lower() == 'q':
                    print("\n" + items, "\n","Total:", total, "Calculated by\n " + name.title())
                    break
                else:
                    print("Invalid input.")
            
            if report.upper() == 'A':
                if userinp.isdigit():
                    total = int(userinp) + total 
                    print (total)
                elif userinp.upper() == 'Q':
                    print("Total:", total)
                    break
                else:
                    print("Invalid input.")
           
            

adding_report("T")