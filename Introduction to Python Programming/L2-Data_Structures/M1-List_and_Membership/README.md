# Lists!

`Data structures` are containers that organize and group data types together in different ways. A list is one of the most common and basic data structures in Python.

You saw here that you can create a list with square brackets. Lists can contain any mix and match of the data types you have seen so far.

```
list_of_random_things = [1, 3.4, 'a string', True]
```

This is a list of 4 elements. All ordered containers (like lists) are indexed in python using a starting index of 0. Therefore, to pull the first value from the above list, we can write:

```
>>> list_of_random_things[0]
1
```

It might seem like you can pull the last element with the following code, but this actually won't work:

```
>>> list_of_random_things[len(list_of_random_things)]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-34-f88b03e5c60e> in <module>()
----> 1 lst[len(lst)]

IndexError: list index out of range
```

However, you can retrieve the last element by reducing the index by 1. Therefore, you can do the following:

```
>>> list_of_random_things[len(list_of_random_things) - 1]
True
```

Alternatively, you can index from the end of a list by using negative values, where -1 is the last element, -2 is the second to last element and so on.

```
>>> list_of_random_things[-1]
True
>>> list_of_random_things[-2]
a string
```

## Slice and Dice with Lists

You saw that we can pull more than one value from a list at a time by using `slicing`. When using slicing, it is important to remember that the `lower` index is `inclusive` and the `upper` index is `exclusive`.

Therefore, this:

```
>>> list_of_random_things = [1, 3.4, 'a string', True]
>>> list_of_random_things[1:2]
[3.4]
```

will only return **3.4** in a list. Notice this is still different than just indexing a single element, because you get a list back with this indexing. The colon tells us to go from the starting value on the left of the colon up to, but not including, the element on the right.

If you know that you want to start at the beginning, of the list you can also leave out this value.

```
>>> list_of_random_things[:2]
[1, 3.4]
```

or to return all of the elements to the end of the list, we can leave off a final element.

```
>>> list_of_random_things[1:]
[3.4, 'a string', True]
```

This type of indexing works exactly the same on strings, where the returned value will be a string.

## Are you `in` OR `not in`?

You saw that we can also use `in` and `not in` to return a bool of whether an element exists within our list, or if one string is a substring of another.

```
>>> 'this' in 'this is a string'
True
>>> 'in' in 'this is a string'
True
>>> 'isa' in 'this is a string'
False
>>> 5 not in [1, 2, 3, 4, 6]
True
>>> 5 in [1, 2, 3, 4, 6]
False
```

## Mutability and Order

**Mutability** is about whether or not we can change an object once it has been created. If an object (like a list or string) can be changed (like a list can), then it is called **mutable**. However, if an object cannot be changed with creating a completely new object (like strings), then the object is considered **immutable**.

```
>>> my_lst = [1, 2, 3, 4, 5]
>>> my_lst[0] = 'one'
>>> print(my_lst)
['one', 2, 3, 4, 5]
```

As shown above, you are able to replace 1 with 'one' in the above list. This is because lists are **mutable**.

However, the following does not work:

```
>>> greeting = "Hello there"
>>> greeting[0] = 'M'
```

This is because strings are `immutable`. This means to change this string, you will need to create a completely new string.

There are two things to keep in mind for each of the data types you are using:

1. Are they `mutable`?
2. Are they `ordered`?

**Order** is about whether the position of an element in the object can be used to access the element. **Both strings and lists are ordered**. We can use the order to access parts of a list and string.

However, you will see some data types in the next sections that will be unordered. For each of the upcoming data structures you see, it is useful to understand how you index, are they mutable, and are they ordered. Knowing this about the data structure is really useful!

Additionally, you will see how these each have different methods, so why you would use one data structure vs. another is largely dependent on these properties, and what you can easily do with it!

## Why Do We Need Lists?

Let's talk about why we need a data structure like a list or when to use it. We will borrow an example from the world of Wall Street for this discussion.

Companies listed on the NASDAQ exchange have ticker symbols or abbreviations for each company name. For e.g., the ticker symbol for Alphabet, Inc. is GOOGL.

Imagine now that you own stocks for one company, say Microsoft, and want to be able to print out the ticker symbol of your stock. Since it is one value, you can store it in the variable **microsoft**, and assign it the value of MSFT. Like this:

```
microsoft = MSFT
```

Well, that's convenient! So, now when you want to print the ticker symbol for the company you hold stocks for, you use the print command.

Let's now consider that you are an investment fund manager, and you want to print out the stocks (or holdings) you own in an index fund (e.g., [Vanguard Institutional Index Fund](https://www.marketwatch.com/investing/fund/vinix/holdings)). An index fund includes stocks (also called holdings) for a large number of companies. Turns out Vanguard Institutional Index Fund has [506 holdings](https://investor.vanguard.com/mutual-funds/profile/VINIX)!

Printing the tickets for all 506 holdings using individual strings would require 506 strings. Not ideal! Because we'll need to remember the name of each string to print it.
You also have to think about how to group the 506 strings under the same index fund. Not convenient at all!

### This is where the beauty of data structures comes into play! You can use a list.

Since index funds have ticker symbols too, you use that as the name for the list, here VINIX, and add the ticker symbols for all the holdings into that list. Let's populate the list with the top holdings listed for [Vanguard Institutional Index Fund](https://www.marketwatch.com/investing/fund/vinix/holdings).

```
VINIX = ['C', 'MA', 'BA', 'PG', 'CSCO', 'VZ', 'PFE', 'HD', 'INTC', 'T', 'V', 'UNH', 'WFC', 'CVX', 'BAC', 'JNJ', 'GOOGL', 'GOOG', 'BRK.B', 'XOM', 'JPM', 'FB', 'AMZN', 'MSFT', 'AAPL']
```

Now, printing the tickers becomes slightly easier. And you don't have to remember the names of the strings!

```
print(VINIX[0])
>>> C
print(VINIX[1])
>>> MA
```

Later you will learn about more efficient ways to print the elements in a list.

You can even use the list to see if a particular stock **is in** the index fund `VINIX` or not.
Like this:

```
'GE' in VINIX
>>> False

'GOOGL' in VINIX
>>> True
```

## Useful Functions for Lists I

- `len()` returns how many elements are in a list.

- `max()` returns the greatest element of the list. How the greatest element is determined depends on what type objects are in the list. The maximum element in a list of numbers is the largest number. The maximum elements in a list of strings is element that would occur last if the list were sorted alphabetically. This works because the the max function is defined in terms of the greater than comparison operator. The max function is undefined for lists that contain elements from different, incomparable types.

- `min()` returns the smallest element in a list. min is the opposite of max, which returns the largest element in a list.

- `sorted()` returns a copy of a list in order from smallest to largest, leaving the list unchanged.

## Useful Functions for Lists II

### `join` method

Join is a string method that takes a list of strings as an argument, and returns a string consisting of the list elements joined by a separator string.

```
new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)
```

> Output

```
fore
aft
starboard
port
```

In this example we use the string `"\n"` as the separator so that there is a newline between each element. We can also use other strings as separators with .join. Here we use a hyphen.

```
name = "-".join(["García", "O'Kelly"])
print(name)
```

> Output

```
García-O'Kelly
```

It is important to remember to separate each of the items in the list you are joining with a comma (,). Forgetting to do so will not trigger an error, but will also give you unexpected results.

### `append` method

A helpful method called `append` adds an element to the end of a list.

```
letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)
```

> Output

```
['a', 'b', 'c', 'd', 'z']
```
