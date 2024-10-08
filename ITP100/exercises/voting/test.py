data = open("voting.txt", "r")
votes = (data.read()).splitlines()
data.close


def count_plur():
    per1 = 0
    per2 = 0
    per3 = 0
    el1 = {'p':0, 'e':0, 12:0, 13:0, 23:0}
    el2 = {'p':0, 'e':0, 12:0, 13:0, 23:0}
    el3 = {'p':0, 'e':0, 12:0, 13:0, 23:0}
    el4 = {'p':0, 'e':0, 12:0, 13:0, 23:0}
    el5 = {'p':0, 'e':0, 12:0, 13:0, 23:0}
    election = 1
    def pick(win, oth, oth2, num):
        if win > oth and win > oth2:
            if election == 1:
                el1['p'] = num
            elif election == 2:
                el2['p'] = num
            elif election == 3:
                el3['p'] = num
            elif election == 4:
                el4['p'] = num
            elif election == 5:
                el5['p'] = num
    for vote in votes: 
        local = str(vote[0])       
        if local =='1':
            per1 += 1
        elif local == '2':
            per2 += 1
        elif local == '3':
            per3 += 1
        elif local == '0' or local == '-':
            pick(per1, per2, per3, 1)
            pick(per2, per1, per3, 2)
            pick(per3, per2, per1, 3)
            per1 = 0
            per2 = 0
            per3 = 0
            election += 1


    def ann(elc, wnr, typ, msg):
        if elc[typ] == wnr:
            print(msg + str(wnr))

    def elect(numb):
        print('-------- election ' + str(numb))
        if numb == 1:
            ann(el1, 1, 'p', 'plurality winner')

#    ann(el1, 1, 'p', 'plurality winner ')
#    ann(el1, 2, 'p', 'plurality winner ')
#    ann(el1, 3, 'p', 'plurality winner ')
    elect(1)
    ann(el2, 1, 'p', 'plurality winner ')
    ann(el2, 2, 'p', 'plurality winner ')
    ann(el2, 3, 'p', 'plurality winner ')

    ann(el3, 1, 'p', 'plurality winner ')
    ann(el3, 2, 'p', 'plurality winner ')
    ann(el3, 3, 'p', 'plurality winner ')

    ann(el4, 1, 'p', 'plurality winner ')
    ann(el4, 2, 'p', 'plurality winner ')
    ann(el4, 3, 'p', 'plurality winner ')

    ann(el5, 1, 'p', 'plurality winner ')
    ann(el5, 2, 'p', 'plurality winner ')
    ann(el5, 3, 'p', 'plurality winner ')

count_plur()
