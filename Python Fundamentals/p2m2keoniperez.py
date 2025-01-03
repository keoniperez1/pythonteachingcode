animals_list = ["dolphin", "cat", "dog", "cow"]
name=  input('Welcome, provide your name please: ')
 
def list_o_matic(animal):
    if animal == "":
        animal = animals_list.pop()
        print("1 instance of", animal, "popped from the list")
    elif animal in animals_list:
        animals_list.remove(animal)
        print("1 instance of", animal, "removed from the list")
    else:
        animals_list.append(animal)
        print("1 instance of", animal, "appended to the list")
     
 
while animals_list:
    animal_choice = input("Welcome, " +name.title()+ " Enter name of an animal, or 'quit' to quit: ")
    if animal_choice.startswith("q"):
        print("Goodbye!") 
        break
    else:
        list_o_matic(animal_choice)
        print("This is the list of animals: ", animals_list)
