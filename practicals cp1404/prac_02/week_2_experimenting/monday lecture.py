"""external students meetup"""

names = "erica, kath, chloe, cobey, mathew".split(", ")
# for name in names:
for i, name in enumerate(names, 1):
    out_file = open(f"files{name}.txt", "a")
    # print(name, file=out_file)
    print(i, file=out_file)
    out_file.close()
