def adding_report(report =""):
    name = input("Welcome, please provide your full name: ")
    total = 0
    items = ""
     
    while True:
        userinp = input("Input a integer or \"Q\" to quit: ")
        if report.upper() == "T":
            if userinp.isdigit():
                total = int(userinp) + total
                items = userinp + items + "\n"
                print(total)
            elif userinp.upper() == "Q":
                print("Total:", total )
                break
        if report.upper() == "A":
            if userinp.isdigit():
                total = int(userinp) + total 
                items = userinp + items + '\n'
                print(total)
            elif userinp.upper() == "Q":
                print("Calculated by:", name.title(), '\n', "Total:", total)
                break

adding_report("A")
