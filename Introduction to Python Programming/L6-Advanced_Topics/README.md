# Iterators and Generators

**Iterables** are objects that can return one of their elements at a time, such as a list. Many of the built-in functions we’ve used so far, like 'enumerate,' return an iterator.

An **iterator** is an object that represents a stream of data. This is different from a **list**, which is also an iterable, but is not an iterator because it is not a stream of data.

**Generators** are a simple way to create iterators using functions. You can also define iterators using **classes**, which you can read more about [here]().

Here is an example of a generator function called `my_range`, which produces an iterator that is a stream of numbers from 0 to (x - 1).

```
def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1
```

Notice that instead of using the return keyword, it uses `yield`. This allows the function to return values one at a time, and start where it left off each time it’s called. This `yield` keyword is what differentiates a generator from a typical function.

Remember, since this returns an iterator, we can convert it to a list or iterate through it in a loop to view its contents. For example, this code:

```
for x in my_range(5):
    print(x)
```

> Output

```
0
1
2
3
4
```

## Why Generators?

You may be wondering why we'd use generators over lists. Here’s an excerpt from a [stack overflow page](https://softwareengineering.stackexchange.com/questions/290231/when-should-i-use-a-generator-and-when-a-list-in-python/290235) that addresses this:

Generators are a lazy way to build iterables. They are useful when the fully realized list would not fit in memory, or when the cost to calculate each list element is high and you want to do it as late as possible. But they can only be iterated over once.

## Generator Expressions

Here's a cool concept that combines generators and list comprehensions! You can actually create a generator in the same way you'd normally write a list comprehension, except with parentheses instead of square brackets. For example:

```
sq_list = [x**2 for x in range(10)]  # this produces a list of squares
print(sq_list)
```

> Output

```
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

```
sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares

print(next(sq_iterator))
print(next(sq_iterator))
print(next(sq_iterator))
```

> Output

```
0
1
4
```
