data = open("voting.txt", "r")
votes = (data.read()).splitlines()
data.close

def count_plur():
    per1 = 0
    per2 = 0
    per3 = 0
    counts = {1:0,2:0,3:0}
    election = 1

    for vote in votes:
        local = int(vote[0])
        if local == 1:
            per1 += 1
        elif local == 2:
            per2 += 1
        elif local == 3:
            per3 += 1
        elif local == 0:
            if per1 > per2 and per1 > per3:
                
            elif per2 > per1 and per2 > per3:
                print("plurality winner 2")
            elif per3 >per1 and per3 >per2:
                print("plurality winner 3")
            continue
        per1 = 0
        per2 = 0
        per3 = 0
        election += 1


count_plur()
