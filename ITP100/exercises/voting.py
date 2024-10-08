data = open("voting.txt", "r")
votes = (data.read()).splitlines()
data.close()


def count_plur():
    per1 = 0
    per2 = 0
    per3 = 0
    for vote in votes:
        local = int(vote[0])
        if local == 1:
            per1 += 1
        elif local == 2:
            per2 += 1
        elif local == 3:
            per3 += 1
        elif local == 0:
            break
    if per1 > per2 and per1 > per3:
        print("plurality winner 1")
    elif per2 > per1 and per2 > per3:
        print("plurality winner 2")
    elif per3 >per1 and per3 >per2:
        print("plurality winner 3")


def count_exhaust():
    per1 = 0
    per2 = 0
    per3 = 0
    for vote in votes:
        local = int(vote[0])
        if local == 1:
            per1 += 1
        elif local == 2:
            per2 += 1
        elif local == 3:
            per3 += 1
        elif local == 0:
            break
    loser = ""
    skip = 0
    if per1 > per2 and per1 > per3 and per2 > per3:
        loser = "per3"
        skip = 3
    elif per2 > per3 and per2 >per1 and per3 > per1:
        loser = "per1"
        skip = 1
    elif per3 > per1 and per3 > per2 and per1 > per2:
        loser = "per2"
        skip = 2
    per1 = 0
    per2 = 0
    per3 = 0
    for vote in votes:
        local = int(vote[0])
        local2 = 0
        if local == 1:
            per1 += 1
        elif local == 2:
            per2 += 1
        elif local == 3:
            per3 += 1
        elif local == skip:
            local2 = int(vote[1])
            if local2 == 1:
                per1 += 1
            elif local2 == 2:
                per2 += 1
            elif local2 == 3:
                per3 += 1
        if local == 0:
            break
    if loser == "per1":
        per1 = 0
    elif loser == "per2":
        per2 = 0
    elif loser == "per3":
        per3 = 0
    if per1 > per2 and per1 > per3:
        print("exhaustive ballot 1")
    elif per2 > per1 and per2 > per3:
        print("exhaustive ballot 2")
    elif per3 >per1 and per3 >per2:
        print("exhaustive ballot 3")


def count_12():
    per1 = 0
    per2 = 0
    per3 = 0
    for vote in votes:
        local = int(vote[0])
        if local == 1:
            per1 += 1
        elif local == 2:
            per2 += 1
        elif local == 0:
            break
    loser = ""
    skip = 0
    if per2 > per1:
        loser = "per1"
        skip = 1
    elif per1 > per2:
        loser = "per2"
        skip = 2
    for vote in votes:
        local = int(vote[0])
        local2 = 0
        if local == 1:
            per1 += 1
        elif local == 2:
            per2 += 1
        elif local == 3:
            per3 += 1
        elif local == skip:
            local2 = int(vote[1])
            if local2 == 1:
                per1 += 1
            elif local2 == 2:
                per2 += 1
            elif local2 == 3:
                per3 += 1
        if local == 0:
            break
    if loser == "per1":
        per1 = 0
    elif loser == "per2":
        per2 = 0
    if per1 > per2 and per1 > per3:
        print("12 primary 1")
    elif per2 > per1 and per2 > per3:
        print("12 primary 2")
    elif per3 >per1 and per3 >per2:
        print("12 primary 3")


def count_13(): 
    per1 = 0
    per2 = 0
    per3 = 0
    for vote in votes:
        local = int(vote[0])
        if local == 1:
            per1 += 1
        elif local == 2:
            per2 += 1
        elif local == 0:
            break
    loser = ""
    skip = 0
    if per1 > per3:
        loser = "per3"
        skip = 3
    elif per3 > per1:
        loser = "per1"
        skip = 1
    for vote in votes:
        local = int(vote[0])
        local2 = 0
        if local == 1:
            per1 += 1
        elif local == 2:
            per2 += 1
        elif local == 3:
            per3 += 1
        elif local == skip:
            local2 = int(vote[1])
            if local2 == 1:
                per1 += 1
            elif local2 == 2:
                per2 += 1
            elif local2 == 3:
                per3 += 1
        if local == 0:
            break
    if loser == "per1":
        per1 = 0
    elif loser == "per2":
        per2 = 0
    if per1 > per2 and per1 > per3:
        print("13 primary 1")
    elif per2 > per1 and per2 > per3:
        print("13 primary 2")
    elif per3 >per1 and per3 >per2:
        print("13 primary 3")


def count_23():
    per1 = 0
    per2 = 0
    per3 = 0
    for vote in votes:
        local = int(vote[0])
        if local == 1:
            per1 += 1
        elif local == 2:
            per2 += 1
        elif local == 0:
            break
    loser = ""
    skip = 0
    if per2 > per3:
        loser = "per3"
        skip = 3
    elif per3 > per2:
        loser = "per2"
        skip = 2
    for vote in votes:
        local = int(vote[0])
        local2 = 0
        if local == 1:
            per1 += 1
        elif local == 2:
            per2 += 1
        elif local == 3:
            per3 += 1
        elif local == skip:
            local2 = int(vote[1])
            if local2 == 1:
                per1 += 1
            elif local2 == 2:
                per2 += 1
            elif local2 == 3:
                per3 += 1
        if local == 0:
            break
    if loser == "per1":
        per1 = 0
    elif loser == "per2":
        per2 = 0
    if per1 > per2 and per1 > per3:
        print("23 primary 1")
    elif per2 > per1 and per2 > per3:
        print("23 primary 2")
    elif per3 >per1 and per3 >per2:
        print("23 primary 3")




def counter():
    count_plur()
    count_exhaust()
    count_12()
    count_13()
    count_23()
counter()
