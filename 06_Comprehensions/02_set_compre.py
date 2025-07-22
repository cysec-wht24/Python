favourite_chais = [
    "Masala Chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elaichi Chai"
]

unique_chai = {chai for chai in favourite_chais }
print(unique_chai)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

result = [[row[i] for row in matrix] for i in range(4)]
print(result)

recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)

# {}: Use when you want a collection of unique, unordered items and don't need duplicates or indexing.

unique_lengths = {len(word) for word in ["hi", "hello", "hi", "bye"]}
print(unique_lengths)  # ➜ {2, 3, 5}