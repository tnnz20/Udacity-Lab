# Quiz: Implement my_enumerate
# Write your own generator function that works like the built-in function enumerate.
lessons = [
    "Why Python Programming", "Data Types and Operators", 
    "Control Flow", "Functions", "Scripting"
    ]

def my_enumerate(iterable, start=0):
    # Implement your generator function here
    while start < len(iterable):
        for i in iterable:
            yield start, i
            start += 1


for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

print()

# Quiz: Chunker
# If you have an iterable that is too large to fit in memory 
# in full (e.g., when dealing with large files), being able to take 
# and use chunks of it at a time can be very valuable.

# Implement a generator function, chunker, that takes in an iterable 
# and yields a chunk of a specified size at a time.

def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

for chunk in chunker(range(25), 4):
    print(list(chunk))

print()
# Generator
sq_list = [x**2 for x in range(10)]  # this produces a list of squares
print(sq_list)

print()
sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares

print(next(sq_iterator))
print(next(sq_iterator))
print(next(sq_iterator))