import random

initial_price = 10.0
max_increase = 0.1
max_decrease = 0.05
min_price = 0.01
max_price = 1000.0

output_file = "stock_output.txt"
out_file = open(output_file, 'w')

price = initial_price
day = 0
print("Starting price: ${:,.2f}".format(price), file=out_file)

while min_price <= price <= max_price:
    price_change = 0
    day += 1
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, max_increase)
    else:
        price_change = random.uniform(-max_decrease, 0)

    price *= (1 + price_change)
    print("On day {} price is: ${:,.2f}".format(day, price), file=out_file)

out_file.close()