# (): generator comprehension aka lazy list are used when you want to use 
# generators and want to generate items one by one without storing them 
# all in memory (for performance).

daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]
# Not usable total_cups = (sale for sale in daily_sales if sale > 5)
# Gives list total_cups = [sale for sale in daily_sales if sale > 5]
total_cups = sum(sale for sale in daily_sales if sale > 5)
print(total_cups)


gen = (x**2 for x in range(5))
for value in gen:
    print(value)  # ➜ 0 1 4 9 16 (one by one)

    