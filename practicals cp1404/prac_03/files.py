"""Q1. Write code that asks the user for their name,
then opens a file called "name.txt" and writes that name to it. Remember to close your file."""

out_file = open("name.txt", "w")
name = input("Please enter your name. ")
out_file.write(name)
out_file.close()

"""Q2.Write code that opens "name.txt" and reads the name (as above) then prints """

in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file. close()
print("your name is", name)

"""Q3. Create a text file called numbers.txt and save it in your prac directory. 
Put the following three numbers on separate lines in the file and save it"""

in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

"""Q4.Now write a fourth block of code that prints the total for all lines in numbers.txt 
or a file with any number of numbers """

in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)