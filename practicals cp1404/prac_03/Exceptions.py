"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("0 cannot be a denominator, please enter a valid denominator."))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#    print("Cannot divide by zero!")
print("Finished.")

# question 1. value error occurs when an integer is not entered.
# question 2/ zero division error occurs when denominator is 0.
# question 3. code can be changed to avoid the possibility. code is already implemented above.
