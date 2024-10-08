list = open("registration_list1.txt", "r")
text = (list.read())
text = text.split()

one = 0        # This is Ravenclaw
two = 0        # This is Hufflepuff
three = 0      # This is Slytherin
four = 0       # This is Gryffindor

def counting(house):
    if items == house:
        if items == 'Ravenclaw':
            global one
            one = one + 1
        if items == 'Hufflepuff':
            global two
            two = two + 1
        if items == 'Slytherin':
            global three
            three = three + 1
        if items == 'Gryffindor':    
            global four
            four = four + 1


for items in text:

    counting('Ravenclaw')
    counting('Hufflepuff')
    counting('Slytherin')
    counting('Gryffindor')





if four < 7:
    print("Gryffindor does not have enough players.")
elif four > 7:
    print("Gryffindor has too many players.")


if one < 7:
    print("Ravenclaw does not have enough players.")
elif one > 7:
    print("Ravenclaw has too many players.")


if three < 7:
    print("Slytherin does not have enough players.")
elif three > 7:
    print("Slytherin has too many players.")


if two < 7:
    print("Hufflepuff does not have enough players.")
elif two > 7:
    print("Hufflepuff has too many players.")


if one == 7 and two == 7 and three == 7 and four == 7:
    print("List complete, let's play quidditch!")



