numbers = [3, 1, 4, 1, 5, 9, 2]

# What values do the following expressions have?
# (solutions not provided; figure it out, then run with print or in console to test)
print(numbers[0])  # lists start at 0.
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])  # last item in the list
print(numbers[3:4])
print(5 in numbers)  # 5 is in th list so its true
print(7 in numbers)  # 7 is not in the list so its false
print("3" in numbers)  # "3" is a string, therefore not in the list that are made of digits.
print(numbers + [6, 5, 3])  # appends to the list at the end

# Write Python expressions (in your Python file) to achieve the following:

# Change the first element of numbers to "ten"
numbers[0] = 10
print(numbers[0])
# Change the last element of numbers to 1
numbers[-1] = 1
print(numbers[-1])
# Get all the elements from numbers except the first two
# print(numbers[2])
print(numbers[2:])
# Check if 9 is an element of numbers
# 9 in numbers
if 9 in numbers:
    print("9 is in numbers list")
else:
    print("9 is not in numbers list")
