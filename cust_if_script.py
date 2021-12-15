#!/usr/bin/env python3

grade = "Your grade is: "

numberGrade = float(input("enter you number:"))

if numberGrade >= 90:
    grade = grade + 'A'
elif numberGrade >= 80:
    grade = grade + 'B'
elif numberGrade >= 70:
    grade = grade + 'C'
elif numberGrade >= 60:
    grade = grade + 'D'
else:
    grade = grade + "You failed try again"
print(grade)


