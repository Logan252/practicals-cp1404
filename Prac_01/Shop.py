def shop():
    total = 0
    number = int(input("please enter number of items: "))
    while number < 0:
        print("invalid number of items")
        number = int(input("please enter number of items: "))
    for i in range(number):
        price = float(input("price of item: "))
        total = total + price
    print("your total is", total)

    if total > 100:
        total *= 0.9  # apply 10% discount
    print("your discounted total is", total)


shop()
