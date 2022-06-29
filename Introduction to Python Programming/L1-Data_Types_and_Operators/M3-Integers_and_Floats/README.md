# Integers and Floats

There are two Python data types that could be used for numeric values:

- int - for integer values
- float - for decimal or floating point values
  You can create a value that follows the data type by using the following syntax:

```
x = int(4.7)   # x is now an integer 4
y = float(4)   # y is now a float of 4.0
```

You can check the type by using the type function:

```
>>> print(type(x))
int
>>> print(type(y))
float
```

Because the float, or approximation, for 0.1 is actually slightly more than 0.1, when we add several of them together we can see the difference between the mathematically correct answer and the one that Python creates.

```
>>> print(.1 + .1 + .1 == .3)
False
```

You can see more on this [here](https://docs.python.org/3/tutorial/floatingpoint.html).

## Python Best Practices

For all the best practices, see the [PEP8 Guidelines](https://peps.python.org/pep-0008/).

You can use the atom package [linter-python-pep8](https://atom.io/packages/linter-python-pep8) to use pep8 within your own programming environment in the Atom text editor, but more on this later. If you aren't familiar with text editors yet, and you are performing all of your programming in the classroom, no need to worry about this right now.

Follow these guidelines to make other programmers and future you happy!

> Good

```
print(4 + 5)
```

> Bad

```
print(                       4 + 5)
```

You should limit each line of code to `80` characters, though `99` is okay for certain use cases. [You can thank IBM for this ruling](https://softwareengineering.stackexchange.com/questions/148677/why-is-80-characters-the-standard-limit-for-code-width).

Why are these conventions important? Although how you format the code doesn’t affect how it runs, following standard style guidelines makes code easier to read and consistent among different developers on a team.

## Divide By Zero?

What happens if you divide by zero in Python? Try it out! Test run this code and see what happens.

```
print(5/0)
```

> Here's what you should have seen when you submitted the Divide by Zero code above:

```
Traceback (most recent call last):
  File "/tmp/vmuser_tnryxwdmhw/quiz.py", line 1, in <module>
    print(5/0)

ZeroDivisionError: division by zero
```

Traceback means "What was the programming doing when it broke"! This part is usually less helpful than the very last line of your error. Though you can dig through the rest of the error, looking at just the final line `ZeroDivisionError`, and the message says we divided by zero. Python is enforcing the rules of arithmetic!

In general, there are two types of errors to look out for

- Exceptions
- Syntax

An Exception is a problem that occurs when the code is running, but a 'Syntax Error' is a problem detected when Python checks the code before it runs it. For more information, see the Python tutorial page on [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html).
