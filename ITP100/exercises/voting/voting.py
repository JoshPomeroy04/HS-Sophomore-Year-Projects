data = open("voting.txt", "r")
votes = (data.read()).splitlines()
data.close()

global per1 
global per2
global per3
per1 = 0
per2 = 0
per3 = 0
global el1 
global el2 
global el3 
global el4 
global el5
el1 = {'p':0, 'e':0, 12:0, 13:0, 23:0}
el2 = {'p':0, 'e':0, 12:0, 13:0, 23:0}
el3 = {'p':0, 'e':0, 12:0, 13:0, 23:0}
el4 = {'p':0, 'e':0, 12:0, 13:0, 23:0}
el5 = {'p':0, 'e':0, 12:0, 13:0, 23:0}
global election
election = 1
def pick(win, oth, oth2, num, chg):
    if win > oth and win > oth2:
        if election == 1:
            el1[chg] = num
        elif election == 2:
            el2[chg] = num
        elif election == 3:
            el3[chg] = num
        elif election == 4:
            el4[chg] = num
        elif election == 5:
            el5[chg] = num

def count_plur():
    per1 = 0
    per2 = 0
    per3 = 0
    election = 1
    for vote in votes:
        local = str(vote[0])
        if local == '1':
            per1 += 1
        elif local == '2':
            per2 += 1
        elif local == '3':
            per3 += 1
        elif local == '0' or local == '-':
            pick(per1, per2, per3, 1, 'p')
            pick(per2, per1, per3, 2, 'p')
            pick(per3, per1, per2, 3, 'p')
            per1 = 0
            per2 = 0
            per3 = 0
            election += 1


def count_exhaust():
    per1 = 0
    per2 = 0
    per3 = 0
    election = 1
    for vote in votes:
        local = str(vote[0])
        if local == '1':
            per1 += 1
        elif local == '2':
            per2 += 1
        elif local == '3':
            per3 += 1
        elif local == '0' or local == '0':
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
                local = str(vote[0])
                local2 = '0'
                if local == '1':
                    per1 += 1
                elif local == '2':
                    per2 += 1
                elif local == '3':
                    per3 += 1
                elif local == skip:
                    local2 = str(vote[1])
                    if local2 == '1':
                        per1 += 1
                    elif local2 == '2':
                        per2 += 1
                    elif local2 == '3':
                        per3 += 1
                elif local == 0:
                        
                    if loser == "per1":
                        per1 = 0
                    elif loser == "per2":
                        per2 = 0
                    elif loser == "per3":
                        per3 = 0
                    pick(per1, per2, per3, 1, 'e')
                    pick(per2, per1, per3, 2, 'e')
                    pick(per3, per2, per1, 3, 'e')
                    per1 = 0
                    per2 = 0
                    per3 = 0
                    election += 1


def count_12():
    per1 = 0
    per2 = 0
    per3 = 0
    election = 1
    for vote in votes:
        local = str(vote[0])
        if local == '1':
            per1 += 1
        elif local == '2':
            per2 += 1
        elif local == '0' or local == '-':
            loser = ""
            skip = 0
            if per2 > per1:
                loser = "per1"
                skip = 1
            elif per1 > per2:
                loser = "per2"
                skip = 2
            for vote in votes:
                local = str(vote[0])
                local2 = '0'
                if local == '1':
                    per1 += 1
                elif local == '2':
                    per2 += 1
                elif local == '3':
                    per3 += 1
                elif local == skip:
                    local2 = str(vote[1])
                    if local2 == '1':
                        per1 += 1
                    elif local2 == '2':
                        per2 += 1
                    elif local2 == '3':
                        per3 += 1
                    elif local == '0' or local == '-':          
                        if loser == "per1":
                            per1 = 0
                        elif loser == "per2":
                            per2 = 0
                        pick(per1, per2, per3, 1, 12)
                        pick(per2, per1, per3, 2, 12)
                        pick(per3, per1, per2, 3, 12)


def count_13(): 
    per1 = 0
    per2 = 0
    per3 = 0
    election = 1
    for vote in votes:
        local = str(vote[0])
        if local == '1':
            per1 += 1
        elif local == '2':
            per2 += 1
        elif local == '0' or local == '-':
            loser = ""
            skip = 0
            if per1 > per3:
                loser = "per3"
                skip = 3
            elif per3 > per1:
                loser = "per1"
                skip = 1
            for vote in votes:
                local = str(vote[0])
                local2 = '0'
                if local == '1':
                    per1 += 1
                elif local == '2':
                    per2 += 1
                elif local == '3':
                    per3 += 1
                elif local == skip:
                    local2 = str(vote[1])
                    if local2 == '1':
                        per1 += 1
                    elif local2 == '2':
                        per2 += 1
                    elif local2 == '3':
                        per3 += 1
                elif local == '0' or local == '-':
                    if loser == "per1":
                        per1 = 0
                    elif loser == "per2":
                        per2 = 0
                    pick(per1, per2, per3, 1, 13)
                    pick(per2, per1, per3, 2, 13)
                    pick(per3, per1, per2, 3, 13)


def count_23():
    per1 = 0
    per2 = 0
    per3 = 0
    election = 1
    for vote in votes:
        local = str(vote[0])
        if local == '1':
            per1 += 1
        elif local == '2':
            per2 += 1
        elif local == '0' or local == '-':
            loser = ""
            skip = 0
            if per2 > per3:
                loser = "per3"
                skip = 3
            elif per3 > per2:
                loser = "per2"
                skip = 2
            for vote in votes:
                local = str(vote[0])
                local2 = '0'
                if local == '1':
                    per1 += 1
                elif local == '2':
                    per2 += 1
                elif local == '3':
                    per3 += 1
                elif local == skip:
                    local2 = str(vote[1])
                    if local2 == '1':
                        per1 += 1
                    elif local2 == '2':
                        per2 += 1
                    elif local2 == '3':
                        per3 += 1
                elif local == '0' or local == '-':
            
                    if loser == "per1":
                        per1 = 0
                    elif loser == "per2":
                        per2 = 0
                    pick(per1, per2, per3, 1, 23)
                    pick(per2, per1, per3, 2, 23)
                    pick(per3, per1, per2, 3, 23)

   
def ann(elc, wnr, typ, msg):
    if elc[typ] == wnr:
        print(msg + str(wnr))
    
    
def elect(numb):
    print('-------- election ' + str(numb))
    if numb == 1:
        ann(el1, 1, 'p', 'plurality winner ')
        ann(el1, 2, 'p', 'plurality winner ')
        ann(el1, 3, 'p', 'plurality winner ')
        ann(el1, 1, 'e', 'exhaustive ballot ')
        ann(el1, 2, 'e', 'exhaustive ballot ')
        ann(el1, 3, 'e', 'exhaustive ballot ')
        ann(el1, 1, 12, '12 primary ')
        ann(el1, 2, 12, '12 primary ')
        ann(el1, 3, 12, '12 primary ')
        ann(el1, 1, 13, '13 primary ')
        ann(el1, 2, 13, '13 primary ')
        ann(el1, 3, 13, '13 primary ')
        ann(el1, 1, 23, '23 primary ')
        ann(el1, 2, 23, '23 primary ')
        ann(el1, 3, 23, '23 primary ')
    if numb == 2:
        ann(el2, 1, 'p', 'plurality winner ')
        ann(el2, 2, 'p', 'plurality winner ')
        ann(el2, 3, 'p', 'plurality winner ')
        ann(el2, 1, 'e', 'exhaustive ballot ')
        ann(el2, 2, 'e', 'exhaustive ballot ')
        ann(el2, 3, 'e', 'exhaustive ballot ')
        ann(el2, 1, 12, '12 primary ')
        ann(el2, 2, 12, '12 primary ')
        ann(el2, 3, 12, '12 primary ')
        ann(el2, 1, 13, '13 primary ')
        ann(el2, 2, 13, '13 primary ')
        ann(el2, 3, 13, '13 primary ')
        ann(el2, 1, 23, '23 primary ')
        ann(el2, 2, 23, '23 primary ')
        ann(el2, 3, 23, '23 primary ')
    if numb == 3:
        ann(el3, 1, 'p', 'plurality winner ')
        ann(el3, 2, 'p', 'plurality winner ')
        ann(el3, 3, 'p', 'plurality winner ')
        ann(el3, 1, 'e', 'exhaustive ballot ')
        ann(el3, 2, 'e', 'exhaustive ballot ')
        ann(el3, 3, 'e', 'exhaustive ballot ')
        ann(el3, 1, 12, '12 primary ')
        ann(el3, 2, 12, '12 primary ')
        ann(el3, 3, 12, '12 primary ')
        ann(el3, 1, 13, '13 primary ')
        ann(el3, 2, 13, '13 primary ')
        ann(el3, 3, 13, '13 primary ')
        ann(el3, 1, 23, '23 primary ')
        ann(el3, 2, 23, '23 primary ')
        ann(el3, 3, 23, '23 primary ')
    if numb == 4:
        ann(el4, 1, 'p', 'plurality winner ')
        ann(el4, 2, 'p', 'plurality winner ')
        ann(el4, 3, 'p', 'plurality winner ')
        ann(el4, 1, 'e', 'exhaustive ballot ')
        ann(el4, 2, 'e', 'exhaustive ballot ')
        ann(el4, 3, 'e', 'exhaustive ballot ')
        ann(el4, 1, 12, '12 primary ')
        ann(el4, 2, 12, '12 primary ')
        ann(el4, 3, 12, '12 primary ')
        ann(el4, 1, 13, '13 primary ')
        ann(el4, 2, 13, '13 primary ')
        ann(el4, 3, 13, '13 primary ')
        ann(el4, 1, 23, '23 primary ')
        ann(el4, 2, 23, '23 primary ')
        ann(el4, 3, 23, '23 primary ')
    if numb == 5:
        ann(el5, 1, 'p', 'plurality winner ')
        ann(el5, 2, 'p', 'plurality winner ')
        ann(el5, 3, 'p', 'plurality winner ')
        ann(el5, 1, 'e', 'exhaustive ballot ')
        ann(el5, 2, 'e', 'exhaustive ballot ')
        ann(el5, 3, 'e', 'exhaustive ballot ')
        ann(el5, 1, 12, '12 primary ')
        ann(el5, 2, 12, '12 primary ')
        ann(el5, 3, 12, '12 primary ')
        ann(el5, 1, 13, '13 primary ')
        ann(el5, 2, 13, '13 primary ')
        ann(el5, 3, 13, '13 primary ')
        ann(el5, 1, 23, '23 primary ')
        ann(el5, 2, 23, '23 primary ')
        ann(el5, 3, 23, '23 primary ')

def counter():
    count_plur()
    count_exhaust()
    count_12()
    count_13()
    count_23()
    elect(1)
    elect(2)
    elect(3)
    elect(4)
    elect(5)
    print(el1)
    print(el2)
    print(el3)
    print(el4)
    print(el5)

counter()
