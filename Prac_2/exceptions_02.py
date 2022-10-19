finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter a valid integer: "))
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)

# experimenting, ignore anything below
num = int(input("please enter a valid number"))
while num not in int:
    print("please enter a valid number")
    # doesnt work
num = int(input("please enter a valid number"))
while num != int:
    print("please enter a valid number")
    # even more broken
