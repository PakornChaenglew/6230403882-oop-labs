name = str(input("Enter a student name:"))

mid = False
final = False

while not mid:
    try:
        score1 = int(input("Enter the student's midterm exam mark (0-100):"))
        if score1 < 0:
            mid = mid
            print("Please enter a valid exam mark (0-100)")
        elif score1 > 100:
            mid = mid
            print("Please enter a valid exam mark (0-100)")
        else:
            mid = True
    except ValueError:
        print("Please enter a valid exam mark (0-100)")
    else:
        mid = mid

while not final:
    try:
        score2 = int(input("Enter the student's final exam mark (0-100):"))
        if score2 < 0:
            final = final
            print("Please enter a valid exam mark (0-100)")
        elif score2 > 100:
            final = final
            print("Please enter a valid exam mark (0-100)")
        else:
            final = True
    except ValueError:
        print("Please enter a valid exam mark (0-100)")
    else:
        final = final

total = (score1 + score2)/2
total = int(total)

if 0 <= total < 50:
    grade = "F"
elif 50 <= total < 60:
    grade = "D"
elif 60 <= total < 70:
    grade = "C"
elif 70 <= total < 80:
    grade = "B"
elif 80 <= total <= 100:
    grade = "A"
print("a has total mark as", total, "and grade as", grade)
