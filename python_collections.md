# Python Collections — Complete Guide
### Theory → Exercises → Projects → Stacked Projects
**How to use this file:**
- Read theory section fully before attempting exercises
- Write every solution with proper functions — no scripts
- Mark each exercise with a comment `# DONE` when complete
- Send back as a single `.py` file with all solutions

---

# PART 1 — LIST

## Theory

A list is an ordered, mutable collection that allows duplicates.
Ordered means items stay in the position you put them.
Mutable means you can change it after creation.

```python
# Creating lists
empty = []
fruits = ["apple", "banana", "cherry"]
mixed = ["alice", 25, True, 3.14]     # can hold any type
nested = [[1, 2], [3, 4], [5, 6]]     # list of lists
```

## Methods

### append(item) — add one item to end
```python
logs = []
logs.append("user logged in")
logs.append("user clicked dashboard")
# → ["user logged in", "user clicked dashboard"]
```

### extend(iterable) — merge another list in
```python
team_a = ["Alice", "Bob"]
team_b = ["Charlie", "Diana"]
team_a.extend(team_b)
# → ["Alice", "Bob", "Charlie", "Diana"]

# extend vs append — know the difference
team_a.append(team_b)
# → ["Alice", "Bob", ["Charlie", "Diana"]]  ← list inside list, wrong!
```

### insert(index, item) — add at specific position
```python
queue = ["Bob", "Charlie"]
queue.insert(0, "Alice")   # Alice jumps to front
# → ["Alice", "Bob", "Charlie"]
```

### remove(item) — remove by value (first occurrence only)
```python
banned = ["spam", "ads", "spam", "clickbait"]
banned.remove("spam")   # removes first "spam" only
# → ["ads", "spam", "clickbait"]

# Safe removal
if "virus" in banned:
    banned.remove("virus")
```

### pop(index) — remove by position AND return it
```python
tasks = ["email", "fix bug", "write docs"]
last = tasks.pop()      # no index = last item
first = tasks.pop(0)    # with index = that position
# pop gives item back, remove doesn't
```

### index(item) — find position of item
```python
students = ["Alice", "Bob", "Charlie"]
print(students.index("Bob"))   # → 1

# Safe usage
if "Diana" in students:
    print(students.index("Diana"))
```

### count(item) — how many times item appears
```python
votes = ["yes", "no", "yes", "yes", "no"]
print(votes.count("yes"))   # → 3
```

### sort() vs sorted() — two different tools
```python
scores = [45, 92, 67, 38, 81]

# sort() — modifies original, returns None
scores.sort()                        # ascending
scores.sort(reverse=True)            # descending

# sorted() — original untouched, returns new list
ranking = sorted(scores, reverse=True)
```

**Rule:** use `sort()` when original doesn't matter. Use `sorted()` when you need original safe.

### reverse() — flip list in place
```python
history = ["page1", "page2", "page3"]
history.reverse()
# → ["page3", "page2", "page1"]
```

### copy() — make independent copy
```python
original = ["Alice", "Bob"]
wrong = original          # NOT a copy — same list!
correct = original.copy() # real independent copy

correct.append("Charlie")
# original untouched → ["Alice", "Bob"]
```

### clear() — empty the list
```python
cart = ["shoes", "shirt"]
cart.clear()   # → []
```

## Slicing — accessing parts of a list
```python
items = ["a", "b", "c", "d", "e"]

items[1:3]    # → ["b", "c"]       from index 1 up to (not including) 3
items[:2]     # → ["a", "b"]       from start to index 2
items[2:]     # → ["c", "d", "e"]  from index 2 to end
items[-2:]    # → ["d", "e"]       last two items
items[::2]    # → ["a", "c", "e"]  every second item
items[::-1]   # → ["e","d","c","b","a"]  reversed copy
```

## Looping Patterns
```python
fruits = ["apple", "banana", "cherry"]

# Basic loop
for fruit in fruits:
    print(fruit)

# With index — use enumerate, not range(len())
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

# Building new list from existing
cleaned = []
for fruit in fruits:
    cleaned.append(fruit.strip().title())

# Filtering
long_fruits = []
for fruit in fruits:
    if len(fruit) > 5:
        long_fruits.append(fruit)
```

## List Comprehension — compact list building
```python
# Basic
squares = [x**2 for x in range(10)]

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# Transforming existing list
names = ["  alice ", "BOB", "charlie  "]
cleaned = [name.strip().title() for name in names]
```

## Nested Lists
```python
# List of lists — think rows and columns
schedule = [
    ["Math", "English", "Science"],   # Monday
    ["History", "Art", "PE"],          # Tuesday
]

# Loop through nested
for day_index, classes in enumerate(schedule, start=1):
    print(f"Day {day_index}:")
    for subject in classes:
        print(f"  - {subject}")
```

## Do's and Don'ts
```
DO:
✓ Use enumerate() instead of range(len())
✓ Use .copy() when you need independence
✓ Use sorted() when original must be preserved
✓ Use slicing to extract parts cleanly
✓ Check membership with 'in' before remove/index

DON'T:
✗ Use append() when you mean extend()
✗ Assign list to new variable thinking it's a copy
✗ Use range(len(list)) when enumerate works
✗ Modify a list while looping through it
✗ Use list for fast lookups — use set or dict instead
```

---

## LIST EXERCISES

**E1 — append + loop**
Ask user to keep entering names until they type "done".
Store in a list. Print all names at the end numbered.
Use functions. One function collects, one displays.

**E2 — extend**
You have two lists of tasks: `urgent` and `normal`.
Write a function that merges them into one list with urgent first.
Print the merged list. Do NOT use + operator — use extend.

**E3 — remove + in**
Store a list of 5 banned usernames hardcoded.
Ask user to enter a username to unban.
If it exists, remove it and confirm. If not, tell them.
Use functions.

**E4 — sort vs sorted**
Ask user to enter 5 numbers.
Show original order, ascending order, descending order.
Original list must stay unchanged throughout.
Use sorted(), not sort().

**E5 — slicing**
Ask user to enter a sentence.
Split into words. Show:
- First 3 words
- Last 3 words
- Every second word
- Sentence reversed word by word
All using slicing, no loops.

**E6 — enumerate**
You have a list of tasks hardcoded.
Display them numbered starting from 1.
User picks a number. Show that task's details.
Validate the number. Use enumerate.

**E7 — copy trap**
Write a function that takes a list of scores, 
sorts it descending and returns top 3.
Original list must be unchanged after calling the function.
Prove it by printing original before and after.

**E8 — nested list**
Build a weekly schedule. 3 days, each day has 3 subjects hardcoded.
Display it formatted (Day 1, Day 2 etc with subjects under each).
Then ask user which day (1-3) and which slot (1-3) they want to change.
Validate both inputs. Update the schedule and display again.

---

## LIST MINI PROJECT

**Student Grade Tracker**

Build a CLI where:
- User can add students (name + score)
- View all students with their grade (A/B/C/D/F based on score)
- See class average
- See highest and lowest scorer
- Remove a student by name

Rules:
- Each student stored as `[name, score]` in a list
- No dicts yet — list only
- Proper functions, no globals
- Validate all inputs
- Handle edge cases (empty list, student not found)

---
---

# PART 2 — TUPLE

## Theory

A tuple is ordered, immutable, allows duplicates.
Immutable means once created it cannot be changed.
Faster than lists. Can be used as dict keys (lists cannot).

```python
# Creating tuples
empty = ()
single = (42,)           # comma required for single item
point = (10, 20)
rgb = (255, 128, 0)
mixed = ("Alice", 25, True)
```

## Why tuples exist — when to use over list

```python
# Use tuple when data should NOT change
DIRECTIONS = ("north", "south", "east", "west")
DAYS = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
RGB_RED = (255, 0, 0)

# Tuples as dict keys — lists cannot do this
grid = {}
grid[(0, 0)] = "start"
grid[(3, 4)] = "end"
grid[(0, 0)]   # → "start"

# Returning multiple values from function — actually a tuple
def get_dimensions():
    return 1920, 1080   # Python packs this as tuple

width, height = get_dimensions()   # unpacking
```

## Unpacking — the main way you use tuples
```python
point = (10, 20)
x, y = point   # clean unpacking

# In loops — very common
students = [("Alice", 95), ("Bob", 72), ("Charlie", 88)]
for name, score in students:
    print(f"{name}: {score}")

# Ignore values with _
coordinates = (10, 20, 30)
x, _, z = coordinates   # ignore y
```

## Methods — only two
```python
data = (1, 2, 2, 3, 2, 4)
data.count(2)    # → 3  how many times 2 appears
data.index(3)    # → 3  position of first 3
```

## Named Tuple — tuple with named fields
```python
from collections import namedtuple

# Define structure once
Point = namedtuple("Point", ["x", "y"])
Student = namedtuple("Student", ["name", "score", "grade"])

# Create instances
p = Point(10, 20)
s = Student("Alice", 95, "A")

# Access by name — clearer than index
print(p.x)       # → 10
print(s.name)    # → Alice
print(s.score)   # → 95

# Still works like regular tuple
print(p[0])      # → 10
x, y = p         # unpacking still works
```

## Do's and Don'ts
```
DO:
✓ Use tuples for data that shouldn't change (coordinates, RGB, config)
✓ Use tuples as dict keys when you need composite keys
✓ Use named tuples when tuple fields need clarity
✓ Unpack tuples in loops for clean readable code
✓ Return multiple values as tuples from functions

DON'T:
✗ Use list when data should be fixed — use tuple
✗ Access tuple items by magic indexes like t[3] — use namedtuple
✗ Forget the comma in single-item tuple: (42,) not (42)
✗ Try to modify a tuple — it will raise TypeError
```

---

## TUPLE EXERCISES

**E1 — basic tuple + unpacking**
Store 3 cities as a tuple: name, country, population.
Unpack and print as: "Tokyo, Japan — population: 13,960,000"
Use a function.

**E2 — tuple as dict key**
You have a grid. Store values at specific coordinates.
Store at least 4 positions with labels like "start", "end", "wall", "treasure".
Write a function that takes a coordinate and returns what's there,
or "empty" if nothing at that coordinate.

**E3 — unpacking in loop**
You have a hardcoded list of tuples: (product, price, quantity).
Write a function that loops through and calculates total value
(price * quantity) for each product and prints a formatted table.
Also returns the grand total.

**E4 — named tuple**
Create a named tuple called `Contact` with fields: name, phone, email.
Create 3 contacts. Store in a list.
Write a function that searches by name and returns the contact,
or None if not found.
Print result formatted: "Name: Alice | Phone: 0300-xxx | Email: alice@x.com"

**E5 — returning multiple values**
Write a function that takes a list of numbers and returns
min, max, average, and count as a tuple.
Unpack the result when calling and display each value.

---

## TUPLE MINI PROJECT

**Leaderboard System**

- Hardcode 5 players as named tuples: name, score, level
- Display sorted leaderboard (highest score first) with rank numbers
- User can search a player by name and see their full details
- Show average score of all players
- Show how many players are above average

Rules:
- Use named tuples for player data
- Use tuple unpacking in all loops
- Proper functions, no globals

---
---

# PART 3 — SET

## Theory

A set is unordered, mutable, no duplicates, fast lookup O(1).
Unordered means no guaranteed position — no indexing.
Main purpose: uniqueness and membership testing.

```python
# Creating sets
empty = set()           # NOT {} — that creates empty dict
fruits = {"apple", "banana", "cherry"}
from_list = set([1, 2, 2, 3, 3, 4])   # → {1, 2, 3, 4}  duplicates gone
```

## Methods

### add(item) — add one item
```python
tags = {"python", "coding"}
tags.add("beginner")
# → {"python", "coding", "beginner"}
```

### remove(item) vs discard(item)
```python
tags = {"python", "coding", "beginner"}

tags.remove("coding")    # raises KeyError if not found
tags.discard("java")     # silent — no error if not found

# Rule: use discard when not sure if item exists
```

### pop() — removes AND returns a random item
```python
items = {"a", "b", "c"}
removed = items.pop()   # random! sets have no order
```

### clear() — empty the set
```python
tags.clear()   # → set()
```

### copy()
```python
backup = tags.copy()
```

## Set Operations — the real power
```python
python_devs = {"Alice", "Bob", "Charlie", "Diana"}
java_devs   = {"Bob", "Diana", "Eve", "Frank"}

# Intersection — in BOTH sets
both = python_devs & java_devs
both = python_devs.intersection(java_devs)
# → {"Bob", "Diana"}

# Union — in EITHER set
all_devs = python_devs | java_devs
all_devs = python_devs.union(java_devs)
# → {"Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"}

# Difference — in first but NOT second
only_python = python_devs - java_devs
only_python = python_devs.difference(java_devs)
# → {"Alice", "Charlie"}

# Symmetric difference — in one but NOT both
exclusive = python_devs ^ java_devs
exclusive = python_devs.symmetric_difference(java_devs)
# → {"Alice", "Charlie", "Eve", "Frank"}
```

## Membership testing — fastest way to check existence
```python
valid_commands = {"add", "remove", "view", "quit"}

user_input = input("Enter command: ").strip().lower()

if user_input in valid_commands:    # O(1) — instant regardless of set size
    print("Valid command")
else:
    print("Unknown command")

# vs list — O(n), slower as list grows
valid_commands_list = ["add", "remove", "view", "quit"]
if user_input in valid_commands_list:   # searches one by one
    ...
```

## Subset and Superset
```python
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

a.issubset(b)     # → True   all of a is in b
b.issuperset(a)   # → True   b contains all of a
a.isdisjoint(b)   # → False  they share elements
```

## Do's and Don'ts
```
DO:
✓ Use set when uniqueness matters
✓ Use set for fast membership testing over list
✓ Use set operations for comparing groups of data
✓ Use discard() over remove() when unsure if item exists
✓ Convert list to set to remove duplicates instantly

DON'T:
✗ Use {} for empty set — that's an empty dict
✗ Rely on set ordering — it has none
✗ Use set when you need to keep duplicates
✗ Use set when you need index access
✗ Use list membership check when set would work
```

---

## SET EXERCISES

**E1 — deduplication**
Ask user to enter 8 words (allow duplicates in input).
Store in a list first. Then convert to set to remove duplicates.
Show how many duplicates were removed (len difference).
Use functions.

**E2 — membership testing**
Build a simple command validator.
Valid commands stored in a set: "add", "remove", "view", "help", "quit".
Keep asking user for commands. If valid, print "Executing: [command]".
If invalid, print "Unknown command. Type 'help' for options."
Stop when user types "quit".

**E3 — set operations**
You have two hardcoded sets: students who passed Math and students who passed Science.
Using set operations find and display:
- Students who passed both
- Students who passed at least one
- Students who passed Math but not Science
- Students who passed only one subject (not both)

**E4 — discard vs remove**
Build a tag manager. Start with 5 hardcoded tags.
User can add a tag, remove a tag (safe — use discard),
or view all tags. Keep running until quit.
Show appropriate message when removing a tag that doesn't exist.

**E5 — convert and compare**
Ask user to enter two sentences.
Find words that appear in both sentences.
Find words unique to each sentence.
Use set operations. Ignore case.

---

## SET MINI PROJECT

**Attendance Tracker**

- Hardcode a class roster of 8 students as a set
- User can mark students present (add to present set)
- Show who is present, who is absent (roster - present)
- Show attendance percentage
- Warn if someone marked present isn't in the roster
- User can remove a student from present (marked in error)

Rules:
- Use set operations throughout
- Proper functions, no globals
- Handle all edge cases

---
---

# PART 4 — DICT

## Theory

A dict is an unordered key-value store, mutable, keys must be unique.
Fast O(1) lookup by key — the most used collection in real projects.

```python
# Creating dicts
empty = {}
person = {"name": "Alice", "age": 25, "city": "Karachi"}
from_pairs = dict(zip(["name", "age"], ["Alice", 25]))
```

## Accessing Values

```python
person = {"name": "Alice", "age": 25}

# Direct — crashes if key missing
person["name"]       # → "Alice"
person["salary"]     # → KeyError CRASH

# .get() — safe, returns None or default
person.get("name")           # → "Alice"
person.get("salary")         # → None
person.get("salary", 0)      # → 0  your default
```

**Rule:** use `[]` only when 100% sure key exists. Use `.get()` otherwise.

## Adding, Updating, Removing

```python
person = {"name": "Alice", "age": 25}

# Add
person["city"] = "Karachi"

# Update one
person["age"] = 26

# Update multiple
person.update({"age": 27, "email": "alice@email.com"})

# Remove and get value
age = person.pop("age")         # → 25, key removed
salary = person.pop("salary", None)  # safe pop with default

# Remove without getting value
del person["city"]

# Clear all
person.clear()
```

## The Three Core Methods

```python
student = {"name": "Bob", "grade": "A", "score": 95}

# .keys()
for key in student.keys():
    print(key)

# .values()
for value in student.values():
    print(value)

# .items() — most used, gives both at once
for key, value in student.items():
    print(f"{key}: {value}")
```

## Checking Existence

```python
config = {"theme": "dark", "language": "english"}

"theme" in config           # → True   key exists
"font_size" not in config   # → True   key missing
"dark" in config.values()   # → True   value exists
```

## setdefault — set only if key missing

```python
settings = {"theme": "dark"}
settings.setdefault("language", "english")  # adds it
settings.setdefault("theme", "light")       # ignored, theme exists
```

## Dict Comprehension

```python
names = ["alice", "bob", "charlie"]

# name → length
lengths = {name: len(name) for name in names}

# With condition
long_names = {name: len(name) for name in names if len(name) > 3}

# Invert a dict
grades = {"Alice": "A", "Bob": "B"}
by_grade = {v: k for k, v in grades.items()}
```

## Nested Dicts

```python
users = {
    "u001": {"name": "Alice", "age": 25, "active": True},
    "u002": {"name": "Bob",   "age": 30, "active": False},
}

# Access
users["u001"]["name"]    # → "Alice"

# Loop
for user_id, info in users.items():
    status = "active" if info["active"] else "inactive"
    print(f"{user_id}: {info['name']} — {status}")

# Add new user
def add_user(users, uid, name, age):
    users[uid] = {"name": name, "age": age, "active": True}

# Update nested value
def deactivate(users, uid):
    if uid not in users:
        print("User not found")
        return
    users[uid]["active"] = False
```

## Common Real Patterns

### Frequency counter
```python
def count_frequency(items):
    frequency = {}
    for item in items:
        frequency[item] = frequency.get(item, 0) + 1
    return frequency
```

### Lookup table — replace long if/elif chains
```python
GRADES = {90: "A", 80: "B", 70: "C", 60: "D"}

def get_grade(score):
    for threshold, grade in sorted(GRADES.items(), reverse=True):
        if score >= threshold:
            return grade
    return "F"
```

### Grouping items
```python
def group_by(items, key_func):
    groups = {}
    for item in items:
        key = key_func(item)
        groups.setdefault(key, [])
        groups[key].append(item)
    return groups
```

## Do's and Don'ts
```
DO:
✓ Use .get() for safe access with a default
✓ Use 'in' to check key existence
✓ Use .items() when you need both key and value
✓ Use setdefault() for grouping patterns
✓ Use name as key, not stored inside value
✓ Store converted types (int not string for numbers)

DON'T:
✗ Use direct [] access without knowing key exists
✗ Use .get(key) as existence check when value could be falsy
✗ Store related data in parallel dicts — nest it
✗ Use generic keys like 'name', 'value' when real name can be key
✗ Mutate dict while iterating over it
```

---

## DICT EXERCISES

**E1 — building a dict correctly**
Ask user for 3 friends and their favourite colours.
Store as `{name: colour}` not `{"name": name, "colour": colour}`.
Print each as "Alice's favourite colour is blue".
Use functions.

**E2 — .get() vs []**
Hardcode a dict of country capitals.
Ask user to enter a country name.
If found, show capital. If not, show "Country not found".
Use .get() — no try/except, no 'in' check.

**E3 — frequency counter**
Ask user to enter a sentence.
Count word frequency manually using .get().
Display sorted most to least frequent.
Use functions. No Counter from collections.

**E4 — .items() loop**
Hardcode a dict of products and prices.
Apply 10% discount to all items.
Display original price and discounted price for each.
Use .items() in loop.

**E5 — setdefault grouping**
You have a hardcoded list of students with subjects:
`[("Alice", "Math"), ("Bob", "Science"), ("Alice", "Science"), ("Charlie", "Math")]`
Group into dict: `{"Math": ["Alice", "Charlie"], "Science": ["Bob", "Alice"]}`
Use setdefault. Print each subject and its students.

**E6 — nested dict**
Build a contact book with nested dicts.
Key is name, value is dict with phone and email.
Functions: add contact, view all, search by name, delete contact.
Validate all inputs.

**E7 — dict comprehension**
Take a list of words from user input.
Build a dict mapping each word to its length.
Then filter to only words longer than 4 characters.
Both using dict comprehension.

**E8 — lookup table**
Build a grade calculator using a lookup table dict.
User enters a score. Function returns letter grade and comment.
Comments: A="Excellent", B="Good", C="Average", D="Passing", F="Fail"
No if/elif chain — dict only.

---

## DICT MINI PROJECT

**Expense Tracker**

- User can add expenses: category, description, amount
- Store as nested dict: `{category: [{description, amount}, ...]}`
- View all expenses grouped by category
- View total per category
- View grand total
- Delete an expense by category and description
- Show which category has highest spending

Rules:
- Nested dict structure required
- Use .get(), .items(), setdefault() appropriately
- Proper functions, no globals
- Validate all inputs (amount must be positive number)

---
---

# PART 5 — COMBINATIONS

## List of Dicts — most common real-world structure
```python
# Like database rows / JSON from APIs
users = [
    {"id": 1, "name": "Alice", "score": 95, "active": True},
    {"id": 2, "name": "Bob",   "score": 72, "active": False},
    {"id": 3, "name": "Clara", "score": 88, "active": True},
]

# Access
users[0]["name"]        # → "Alice"

# Loop
for user in users:
    print(user["name"], user["score"])

# Filter
active_users = [u for u in users if u["active"]]

# Sort by score
sorted_users = sorted(users, key=lambda u: u["score"], reverse=True)

# Find one user
def find_user(users, name):
    for user in users:
        if user["name"] == name:
            return user
    return None
```

## Dict of Lists — grouping pattern
```python
schedule = {
    "Monday":  ["Math", "English", "Science"],
    "Tuesday": ["History", "Art", "PE"],
}

# Add to a day
schedule["Monday"].append("Lunch")

# Loop
for day, subjects in schedule.items():
    print(f"{day}:")
    for subject in subjects:
        print(f"  - {subject}")
```

## Dict of Dicts — keyed records
```python
employees = {
    "E001": {"name": "Alice", "dept": "Engineering", "salary": 90000},
    "E002": {"name": "Bob",   "dept": "Marketing",   "salary": 75000},
}

# Access
employees["E001"]["salary"]   # → 90000

# Add field to all
for emp in employees.values():
    emp["bonus"] = emp["salary"] * 0.1
```

## List of Tuples — fixed records
```python
# Common for returning data from databases
records = [("Alice", 95, "A"), ("Bob", 72, "B"), ("Clara", 88, "B")]

for name, score, grade in records:
    print(f"{name}: {score} ({grade})")
```

## Converting Between Collections
```python
# List → Set (remove duplicates)
items = [1, 2, 2, 3, 3]
unique = set(items)

# Set → List (when you need ordering/indexing)
sorted_unique = sorted(unique)

# List of tuples → Dict
pairs = [("Alice", 95), ("Bob", 72)]
grades = dict(pairs)

# Dict → List of tuples
items = list(grades.items())   # → [("Alice", 95), ("Bob", 72)]

# Dict → sorted list of tuples
sorted_items = sorted(grades.items(), key=lambda x: x[1], reverse=True)

# Two lists → Dict
names = ["Alice", "Bob"]
scores = [95, 72]
combined = dict(zip(names, scores))
```

---

## COMBINATIONS EXERCISES

**E1 — list of dicts**
Hardcode a list of 4 products (each a dict with name, price, category).
Write functions to:
- Display all products
- Filter by category
- Find most expensive product
- Sort by price ascending

**E2 — dict of lists**
Build a playlist manager.
Dict structure: `{genre: [song1, song2, ...]}`
User can add genre, add song to genre, view all genres,
view songs in a genre. Use setdefault for adding songs.

**E3 — converting**
Ask user to enter 6 words (duplicates allowed).
Show them as: original list, unique set, sorted list, 
frequency dict (word: count), and top 3 most frequent.
One pipeline of conversions.

**E4 — list of dicts sorting and filtering**
Hardcode 5 students: name, score, subject.
Write functions:
- Show all sorted by score descending
- Show only students above average
- Group by subject (dict of lists)
- Find top student per subject

---

## COMBINATIONS MINI PROJECT

**Library Book Manager**

Structure: dict of lists → `{genre: [book_dicts]}`
Each book: `{"title": str, "author": str, "available": bool}`

Features:
- Add a book to a genre
- View all books by genre
- Search book by title across all genres
- Borrow a book (set available to False)
- Return a book (set available to True)
- Show all available books
- Show stats: total books, total available, per-genre count

Rules:
- Must use nested combination (dict of lists of dicts)
- Proper functions, no globals
- Full input validation

---
---

# PART 6 — ADVANCED COLLECTIONS (collections module)

## defaultdict — no KeyError, auto-creates defaults

```python
from collections import defaultdict

# No more setdefault needed for grouping
groups = defaultdict(list)
students = [("Alice", "Math"), ("Bob", "Science"), ("Alice", "Science")]
for name, subject in students:
    groups[subject].append(name)
# → {"Math": ["Alice"], "Science": ["Bob", "Alice"]}

# defaultdict(int) for counting
counter = defaultdict(int)
words = ["apple", "banana", "apple", "cherry", "apple"]
for word in words:
    counter[word] += 1   # no .get() needed, starts at 0 automatically
```

## Counter — count anything instantly

```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = Counter(words)
# → Counter({"apple": 3, "banana": 2, "cherry": 1})

count.most_common(2)     # → [("apple", 3), ("banana", 2)]
count["apple"]           # → 3
count["missing"]         # → 0  no KeyError

# Combine counters
c1 = Counter({"a": 3, "b": 2})
c2 = Counter({"a": 1, "c": 4})
c1 + c2   # → Counter({"c": 4, "a": 4, "b": 2})
c1 - c2   # → Counter({"b": 2, "a": 2})

# Anagram check
def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
```

## deque — fast insert/remove from BOTH ends

```python
from collections import deque

# List pop(0) is O(n) — slow. deque popleft() is O(1) — fast.
queue = deque()
queue.append("task1")      # add to right
queue.append("task2")
queue.popleft()            # remove from left O(1)

queue.appendleft("urgent") # add to left
queue.pop()                # remove from right

# Max length — auto-removes oldest when full
recent = deque(maxlen=5)
for i in range(10):
    recent.append(i)
# → deque([5, 6, 7, 8, 9])  only last 5 kept
```

## OrderedDict — dict that remembers insertion order + move_to_end

```python
from collections import OrderedDict

# Regular dicts maintain insertion order since Python 3.7
# OrderedDict is useful for move_to_end — needed for LRU cache pattern
od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3

od.move_to_end("a")          # move "a" to end
od.move_to_end("c", last=False)  # move "c" to front
od.popitem(last=False)       # remove first item
od.popitem()                 # remove last item
```

## namedtuple — already covered in tuple section

## Do's and Don'ts
```
DO:
✓ Use Counter instead of manual frequency counting
✓ Use defaultdict(list) for grouping instead of setdefault
✓ Use defaultdict(int) for counting instead of .get(k, 0)
✓ Use deque for queues — not list with pop(0)
✓ Use deque(maxlen=n) for fixed-size recent history

DON'T:
✗ Import collections module for basic tasks lists/dicts handle
✗ Use OrderedDict just for ordering — regular dict does that now
✗ Use Counter when a simple .get() count suffices
✗ Use deque when you only need one-end operations (use list)
```

---

## ADVANCED COLLECTIONS EXERCISES

**E1 — defaultdict(list)**
Hardcode a list of (student, subject, grade) tuples.
Group by subject using defaultdict.
Print each subject with all student grades under it.

**E2 — defaultdict(int)**
Ask user to enter a paragraph of text.
Count word frequency using defaultdict(int).
Show top 5 most frequent words.

**E3 — Counter**
Ask user to enter two sentences.
Use Counter on each.
Show words that appear more in sentence 1 than sentence 2
and vice versa using counter subtraction.

**E4 — deque as queue**
Simulate a print queue.
User can add documents to queue, process next document (popleft),
view current queue, or quit. Use deque.

**E5 — deque maxlen**
Simulate a browser history with max 5 pages.
User keeps entering URLs. Show current history after each addition.
When visiting a new URL after 5, oldest drops automatically.

**E6 — Counter anagram**
Ask user to enter two words.
Tell them if they're anagrams using Counter.
Also show which letters differ if not anagram.

---

## ADVANCED MINI PROJECT

**Word Analysis Tool**

User enters a text (multiline, until they type "END").

Show:
- Top 10 most common words (Counter)
- Top 5 most common characters excluding spaces (Counter)
- Words grouped by first letter (defaultdict)
- Unique words count
- Most recent 5 words entered (deque maxlen)
- Check if any two words in text are anagrams of each other

Rules:
- Must use Counter, defaultdict, and deque
- Case insensitive
- Strip punctuation from words
- Proper functions

---
---

# FINAL STACKED PROJECT

## Task Management System

This project uses everything: list, tuple, set, dict,
list of dicts, defaultdict, Counter, proper functions,
exception handling, and validation.

**Data structure:**
```python
# Each task stored as dict in a list
tasks = [
    {
        "id": 1,
        "title": "Fix login bug",
        "category": "Engineering",
        "priority": "high",       # high, medium, low
        "status": "pending",      # pending, in_progress, done
        "tags": {"bug", "urgent"} # set of tags
    }
]
```

**Features to build:**

1. Add task — title, category, priority (validate: must be high/medium/low), tags (comma separated, stored as set)
2. View all tasks — formatted table
3. Filter tasks — by status, by priority, by category, by tag
4. Update task status — pending → in_progress → done
5. Delete task by ID
6. Statistics dashboard showing:
   - Count per status (use Counter)
   - Count per category (use Counter)
   - Count per priority
   - All unique tags across all tasks (use set union)
   - Most common tag
7. Search tasks by keyword in title
8. Export summary — grouped by category (use defaultdict)

**Rules:**
- Proper functions for every operation
- No globals — data lives in main and passes through parameters
- Full validation on all inputs
- Exception handling where appropriate
- Every function does one job
- Use the right collection for the right job throughout

---

**When you're done with everything:**
Send back one `.py` file.
Each part separated by a comment block like:

```python
# ================================================================
# PART 1 — LIST EXERCISES
# ================================================================

# E1
def collect_names(): ...

# E2
def merge_tasks(): ...
```

Good luck. Take as many days as you need.
```
