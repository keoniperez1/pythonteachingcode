new_words= []
def poem_mixer(list1):
    list1.sort()
    while True:
        if len(list1)> 5:
            new_words.append(list1.pop(-5))
            new_words.append(list1.pop(0))
            new_words.append(list1.pop())
        else:
            return new_words
        
inpuser = input('Provide a poem: ')
list1 = inpuser.split()
lenght = len(list1)
for wyz in range(0, lenght):
    if len(list1[wyz])<=3:
        list1[wyz] = list1[wyz].lower()
    elif len(list1[wyz])>=7:
        list1[wyz] = list1[wyz].upper()
print(" ".join(poem_mixer(list1)))