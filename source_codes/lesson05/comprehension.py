
# List comprehension
my_list = [x for x in range(20) if x % 2 == 0]
print(my_list)

prices = {'apple': 1.0, 'banana': 0.5}
discounted_prices = {item: price * 0.9 for item, price in prices.items()}
print(discounted_prices)