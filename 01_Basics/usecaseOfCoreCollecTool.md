# Core Built-in Collection Data Types in Python

---

## List

### When to use:
- You need an ordered, mutable sequence.
- You may want to append/remove elements frequently.
- Duplicates are fine.

### Example Use Cases:
- Storing items in a user's shopping cart.
- Collecting results from a loop.
- Representing a row of data from a CSV file.

```python
shopping_cart = ['laptop', 'mouse', 'laptop']
shopping_cart.append('keyboard')
```

## Tuple

### When to use:
- You want an ordered, immutable sequence.
- The data shouldn't change after creation.
- Used as dictionary keys, or to ensure hashability.

### Example Use Cases:
- Representing a fixed set of coordinates.
- Storing configuration values.
- Returning multiple values from a function.

```python 
coordinates = (28.6139, 77.2090)  # latitude, longitude
user = ('Manomay', 20, 'India')
```

## Set
### When to use:
- You want a collection of unique elements.
- You need to perform set operations (union, intersection).
- Order does not matter.

### Example Use Cases:
- Removing duplicates from a list.
- Checking for common tags between posts.
- Storing all users who liked a post.

```python
unique_tags = set(['python', 'ai', 'python', 'dev'])
common_tags = tag_set_1 & tag_set_2  # intersection
```

## Dictionary (dict)
### When to use:
- You need a mapping between keys and values.
- Keys must be unique, and lookup should be fast.

### Example Use Cases:
- Storing user profile info (name, age, email).
- Representing JSON-like data.
- Creating a lookup table for configurations.

```python
user_profile = {
    'name': 'Manomay',
    'age': 20,
    'email': 'manomay@example.com'
}
```

## String (str)
### When to use:
- You’re working with text (e.g., names, addresses, messages).
- Need to do parsing, formatting, or matching.

### Example Use Cases:
- Reading and writing files.
- Formatting user input or messages.
- Constructing URLs or queries.

```python
message = f"Welcome {user_profile['name']}!"
query = "SELECT * FROM users WHERE name = 'Manomay'"
```