def adding_report(report = ""): 
    name = input("Please provide your full name: ")
    total= 0
    items = "items\n"

    while True:
            userinp= input("Enter a integer or \"Q\" to quit: ")
            if report.upper() == 'T':
                if userinp.isdigit():
                    total = int(userinp) + total  
                    print(total)
                elif userinp.lower() == 'q':
                    print(total, "Calculated by\n ", name)
                    break
            if report.upper() == 'A':
                if userinp.isdigit():
                    total = int(userinp) + total 
                    print (total)
                elif userinp.upper() == 'Q':
                    print("Total: ", total)
                    break

adding_report("T")