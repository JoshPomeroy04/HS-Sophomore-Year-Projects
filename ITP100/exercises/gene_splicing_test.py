list = open("gene_splicing_test.txt", "r")
text = (list.read())
text = text.splitlines()
count = 0
items = dict()

for thing in text:    # Splits up the document into a dictionary by line
    if thing not in items:
        items[thing] = count
        count = count + 1

def get_key(val, group):    # Returns the key based off the value of the key
    for key, value in group.items(): 
         if val == value: 
             return key 

# Putting each item of the dictionary into a variable
one = get_key(1, items)
two = get_key(2, items)
three = get_key(3, items)
four = get_key(4, items)
five = get_key(5, items)
six = get_key(6, items)
seven = get_key(7, items)
eight = get_key(8, items)
nine = get_key(9, items)
ten = get_key(10, items)
eleven = get_key(11, items)
twelve = get_key(12, items)

# Splits the line in the variable into a list: Splits "1 1 2 .0001" into "1", "1", "2", ".0001"
one = one.split()
two = two.split()
three = three.split()
four = four.split()
five = five.split()
six = six.split()
seven = seven.split()
eight = eight.split()
nine = nine.split()
ten = ten.split()
eleven = eleven.split()
twelve = twelve.split()


def test(number):   # Function that does the splicing
    A = float(number[0])
    B = float(number[1])
    toler = float(number[3])
    remove = float(number[2])
    end = A / B
    groupA = 1
    groupB = 0
    test_num = 0
    while ((groupB / (1 - groupB) - end) < -1 * toler) or ((groupA / (1 - groupA) - end) > toler): # Runs while A/B isn't within the tolerance
        groupB = (groupB * B + groupA * remove) / (B + remove) # Moves from A to B
        groupA = (groupA * (A - remove) + groupB * remove) / A # Moves from B to A
        test_num += 1
    print(test_num)


        
test(one)
test(two)
test(three)
test(four)
test(five)
test(six)
test(seven)
test(eight)
test(nine)
test(ten)
test(eleven)
test(twelve)
