list = open("registration_list1.txt", "r")
text = (list.read())
text = text.split()

objects = dict()

Rvn = 0        
Huffl = 0        
Slyth = 0      
Gryff = 0       

for name in text:
    if name not in objects:
        objects[name] = 1
    else:
        objects[name] = objects[name] + 1

Rvn = objects.get('Ravenclaw')
Huffl = objects.get('Hufflepuff')
Slyth = objects.get('Slytherin')
Gryff = objects.get('Gryffindor')


if Gryff < 7:
    print("Gryffindor does not have enough players.")
elif Gryff > 7:
    print("Gryffindor has too many players.")


if Rvn < 7:
    print("Ravenclaw does not have enough players.")
elif Rvn > 7:
    print("Ravenclaw has too many players.")


if Slyth < 7:
    print("Slytherin does not have enough players.")
elif Slyth > 7:
    print("Slytherin has too many players.")


if Huffl < 7:
    print("Hufflepuff does not have enough players.")
elif Huffl > 7:
    print("Hufflepuff has too many players.")


if Gryff == 7 and Rvn == 7 and Slyth == 7 and Huffl == 7:
    print("List complete, let's play quidditch!")

