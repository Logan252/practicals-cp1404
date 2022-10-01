"""
get a valid score (must be 0-100 inclusive)
print result (copy or import your function from score.py)
print stars (this should print as many stars as the score)
quit
"""


def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        score = float(input("Enter a valid score: "))
    print(grade(score))


def grade(score):
    if score >= 90:
        return "excellent"
    elif score >= 50:
        return "passable"
    else:
        return "bad"


main()
