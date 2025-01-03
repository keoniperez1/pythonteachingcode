def str_analysis():
    username= input("Say your full name: ")
    while True:
        userans= input("Say a number or word!: ")
        if userans.isdigit():
            if int(userans) > 99:
                print(username.title(), "That's a big number!")
                break
            else:
                print(username.title(),"That is a small number!")
            break
        elif userans.isalpha():
            print(username.title(),"That's all alphabetic characters!")
            break
        else:
            print("That is not a valid input. ")

str_analysis()