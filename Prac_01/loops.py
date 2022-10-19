def loops():
    for i in range(1, 21, 2):
        print(i, end=' ')
    print()

    for i in range(0, 110, 10):
        print(i, end=' ')
    print()

    for i in range(20, 0, -1):
        print(i, end=' ')
    print()
    # * multiplies the string by the number inputted
    star_num = int(input("please enter the number of stars"))
    print('*' * star_num)
    # now need to put the number inputted into a range
    star_num = int(input("please enter the number of stars"))
    for i in range(star_num):
        print('*' * star_num)
        star_num = star_num - 1
    # now for the other way
    star_num = int(input("please enter the number of stars"))
    star_count = 1
    for star_count in range(star_num + 1):
        print('*'*star_count)


loops()
