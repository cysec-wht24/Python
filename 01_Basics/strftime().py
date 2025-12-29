# It converts a date/time object → string using special format codes.
from datetime import datetime

now = datetime.now()
print(now.strftime("%Y-%m-%d"))

# the % denotes the next charecter as the formatting code
# | Code | Meaning       | Example |
# | ---- | ------------- | ------- |
# | `%Y` | 4-digit year  | 2025    |
# | `%y` | 2-digit year  | 25      |
# | `%m` | Month (01–12) | 01      |
# | `%d` | Day (01–31)   | 30      |
# | `%H` | Hour (24h)    | 14      |
# | `%I` | Hour (12h)    | 02      |
# | `%M` | Minute        | 45      |
# | `%S` | Second        | 09      |
# | `%p` | AM / PM       | PM      |

# strptime(): string ➜ datetime opposite of strftime()
date_str = "2025-01-30 18:45:10"
dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(dt)
