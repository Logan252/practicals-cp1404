def main():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        score = float(input("Enter a valid score: "))
    print(grade(score))
    print_asterisks(score)


def grade(score):
    if score >= 90:
        return "excellent"
    elif score >= 50:
        return "passable"
    else:
        return "bad"


def print_asterisks(score):
    print('*' * score)


main()
