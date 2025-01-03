def program_g():
    word1 =""
    name = input("Provide your full name: ")
    user1= input("Welcome, " + name.title() + ": enter a sentence quote, non-alpha separate words: ")
    for word in user1:
        if word.isalpha():
            word1 += word
        else:
            if word1.lower()>= "h":
                print(word1.upper())
                word1 = ""
            else:
                word1 = ""
        
program_g()