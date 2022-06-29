# Type and Type Conversion

You have seen four data types so far:

1. `int`
2. `float`
3. `bool`
4. `string`

You got a quick look at `type()` from an earlier video, and it can be used to check the data type of any variable you are working with.

```
>>> print(type(633))
int
>>> print(type(633.0))
float
>>> print(type('633'))
str
>>> print(type(True))
bool
```

You saw that you can change variable types to perform different operations. For example,

```
>>> "0" + "5"
05
```

provides completely different output than

```
>>> 0 + 5
5
```

```
>>> 0 + "5"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
