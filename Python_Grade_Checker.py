def grade_Checker(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print ("Enter your score ")
score = int(input())

grade = grade_Checker(score)

print ("Your grade is: " + grade)
