>>> result = 1/3.0
>>> result
0.3333333333
>>> repr('chai')
"'chai'"
>>> str('chai')
'chai'
>>> print('chai')
chai
>>> 

Difference between `repr()`, `str()`, and `print()` in Python lies in **how objects are converted to strings**—especially when representing vs displaying them:

---

### ✅ `repr(obj)` — **Official Representation**  
- Returns a **string that would ideally allow the object to be recreated** (or shows the internal representation).
- Used mostly for **debugging** and **developers**.
- Strings are shown **with quotes**, and special characters (like `\n`, `\t`) are escaped.

```python
repr('chai')  # Output: "'chai'"  ← with quotes
```

---

### ✅ `str(obj)` — **User-Friendly String**  
- Returns a **nicely printable version** of the object.
- Used for **end-user display**, like logs or UI.
- Quotes are **not** shown for strings.

```python
str('chai')  # Output: 'chai'  ← no quotes
```

---

### ✅ `print(obj)` — **Outputs str(obj)**  
- It’s **just a function that calls `str()`** under the hood and writes it to the console.
- It outputs the final result **visibly**, not as a return value.

```python
print('chai')  # Output shown: chai  ← raw text to console
```

---

### 🔍 Summary Table

| Expression      | Purpose              | Output                       |
|-----------------|----------------------|------------------------------|
| `repr('chai')`  | Developer-friendly   | `"'chai'"`                   |
| `str('chai')`   | User-friendly        | `'chai'`                     |
| `print('chai')` | Console output       | `chai`                       |

---

### Example With a Custom Object

```python
class Tea:
    def __repr__(self):
        return "Tea('chai')"
    def __str__(self):
        return "A hot cup of chai"

t = Tea()
print(repr(t))  # Tea('chai')
print(str(t))   # A hot cup of chai
print(t)        # A hot cup of chai (because print uses str)
```

The bin() function in Python converts an integer to its binary representation (as a string, prefixed with '0b').

Explore libraries
-> random
-> from decimal import Decimal
-> from fractions import Fractions
