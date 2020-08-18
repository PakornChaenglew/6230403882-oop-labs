A = False

while not A:
    try:
        score1 = input("Enter the first number:")
        if score1 == "quit":
            A = False
        score1 = int(score1)
        if score1 <= 0 and score1 >= 0:
            A = True
        score2 = input("Enter the second number:")
        if score2 == "quit":
            A = False
        score2 = int(score2)
        if score2 <= 0 and score2 >= 0:
            A = True
        operator = input("Enter the operator:")
        operator = str(operator)
        if operator == "+":
            ans = score1 + score2
        score2 = int(score2)
        if operator == "-":
            ans = score1 - score2
        if operator == "*":
            ans = score1 * score2
        if operator == "/":
            if score2 == 0:
                print("Error. integer division or modulo by zero")
                break
            ans = score1 / score2
        if operator == "//":
            if score2 == 0:
                print("Error. integer division or modulo by zero")
                break
            ans = score1 // score2
        print(score1, operator, score2, "=", ans)
    except ValueError:
        print("Error")
