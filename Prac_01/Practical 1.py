def sales_bonus():
    # need a salary to know what to apply the bonus to
    salary = float(input("please enter your salary"))
    sales = float(input("please enter your sales"))
    if sales < 1000:
        bonus = salary * 0.1
        salary = salary + bonus
        print(salary)
    else:
        bonus = salary * 0.15
        print(salary)


sales_bonus()


def grade():
    # check for valid input
    score = float(input("Enter score: "))
    while score not in range(0, 100):
        print("please add a valid score")
        score = float(input("Enter score: "))
    if 49 < score < 91:
        print("Passable")
    elif score > 90:
        print("Excellent")
    else:
        print("Bad")


grade()
