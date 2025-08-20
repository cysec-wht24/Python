# Generally, float('inf') and float('-inf') are preferred for comparisons in Python.

import sys

max_int = sys.maxsize        # 9223372036854775807 on most systems
min_int = -sys.maxsize - 1   # -9223372036854775808

print(max_int)
print(min_int)