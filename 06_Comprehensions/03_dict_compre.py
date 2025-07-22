tea_prices_inr = {
    "Masala Chai": 40,
    "Green Tea": 50,
    "Lemon Tea": 200
}

tea_prices_usd = {tea:price / 80 for tea, price in tea_prices_inr.items()}
print(tea_prices_usd)

# {}: For dictionary use when you want to create a mapping from keys to values.

squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # ➜ {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}