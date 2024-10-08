score = input("Enter Score: ")
score = float(score)

if score > 1 or score < 0:
    print("I'm sorry this number is not between 0.0 and 1.0.")
elif score >= 0.9:
    print("Your letter grade is an A.")
elif score >= 0.8:
    print("Your letter grade is a B.")
elif score >= 0.7:
    print("Your letter grade is a C.")
elif score >= 0.6:
    print("Your letter grade is a D.")
elif score < 0.6:
    print("Your letter grade is a F.")
