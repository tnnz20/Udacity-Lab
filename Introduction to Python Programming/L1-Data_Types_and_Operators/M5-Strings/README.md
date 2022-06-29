# Strings

Strings in Python are shown as the variable type `str`. You can define a string with either double quotes `"` or single quotes `'`. If the string you are creating actually has one of these two values in it, then you need to be careful to assure your code doesn't give an error.

```
>>> my_string = 'this is a string!'
>>> my_string2 = "this is also a string!!!"
```

You can also include a `\` in your string to be able to include one of these quotes:

```
>>> this_string = 'Simon\'s skateboard is in the garage.'
>>> print(this_string)
```

> Output

```
Simon's skateboard is in the garage.
```

If we don't use this, notice we get the following `error`:

```
>>> this_string = 'Simon's skateboard is in the garage.'

  File "<ipython-input-20-e80562c2a290>", line 1
    this_string = 'Simon's skateboard is in the garage.'
                         ^
SyntaxError: invalid syntax
```

```
>>> first_word = 'Hello'
>>> second_word = 'There'
>>> print(first_word + second_word)

HelloThere

>>> print(first_word + ' ' + second_word)

Hello There

>>> print(first_word * 5)

HelloHelloHelloHelloHello

>>> print(len(first_word))

5
```

Unlike the other data types you have seen so far, you can also index into strings, but you will see more on this soon! For now, here is a small example. Notice Python uses 0 indexing - we will discuss this later in this lesson in detail.

```
>>> first_word[0]

H

>>> first_word[1]

e
```

## The `len()` function

`len()` is a built-in Python function that returns the length of an object, like a string. The length of a string is the number of characters in the string. This will always be an integer.

There is an example above, but here's another one:

```
print(len("ababa") / len("ab"))
2.5
```

You know what the data types are for `len("ababa")` and `len("ab")`. Notice the data type of their resulting quotient here.

> More Informations about len() Functions

`len` only works on a "sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set)," as per the [Python documentation](https://docs.python.org/2/library/functions.html#len).
