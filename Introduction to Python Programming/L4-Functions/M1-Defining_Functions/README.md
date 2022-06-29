# Defining Functions

Example of a function definition:

```
def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2
```

After defining the cylinder_volume function, we can **call** the function like this.

```
cylinder_volume(10, 3)
```

This is called a **function call** statement.

A function definition includes several important parts.

## Function Header

Let's start with the function header, which is the first line of a function definition.

1. The function header always starts with the `def` keyword, which indicates that this is a **function definition**.
2. Then comes the **function name** (here, `cylinder_volume`), which follows the same naming conventions as variables. You can revisit the naming conventions below.
3. Immediately after the name are parentheses that may include **arguments** separated by commas (here, `height` and `radius`). Arguments, or **parameters**, are values that are passed in as **inputs** when the function is called, and are used in the function body. If a function doesn't take arguments, these parentheses are left empty.
4. The header always end with a colon `:`.

## Function Body

The rest of the function is contained in the body, which is where the function does its work.

1. The **body** of a function is the code indented after the header line. Here, it's the two lines that define and `return` the volume.
2. Within this body, we can refer to the **argument variables** and define new variables, which can only be used within these indented lines.
3. The body will often include a `return` statement, which is used to send back an **output value** from the function to the statement that called the function. A `return` statement consists of the `return` keyword followed by an expression that is evaluated to get the output value for the function. If there is no `return` statement, the function simply returns None.
   Below, you'll find a code editor where you can experiment with this.

## Naming Conventions for Functions

Function names follow the same naming conventions as variables.

1. Only use ordinary letters, numbers and underscores in your function names. They can’t have spaces, and need to start with a letter or underscore.
2. You can’t use Python's reserved words or keywords for function names, as discussed earlier with variable names. Here again is that [table of Python's reserved words](https://docs.python.org/3/reference/lexical_analysis.html#keywords).
3. Try to use descriptive names that can help readers understand what the function does.

## Print vs Return in Functions

```
# this prints something, but does not return anything
def show_plus_ten(num):
    print(num + 10)

print('Calling show_plus_ten...')
return_value_1 = show_plus_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_1))
```

> Ouput

```
Calling show_plus_ten... 15 Done calling This function returned: None
```

```
# this returns something
def add_ten(num):
    return(num + 10)

print('\nCalling add_ten...')
return_value_2 = add_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_2))
```

> Output

```
Calling add_ten... Done calling This function returned: 15
```

## Default Arguments

We can add default arguments in a function to have default values for parameters that are unspecified in a function call.

```
def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2
```

In the example above, `radius` is set to 5 if that parameter is omitted in a function call. If we call `cylinder_volume(10)`, the function will use 10 as the height and 5 as the radius. However, if we call `cylinder_volume(10, 7)` the 7 will simply overwrite the default value of 5.

Also notice here we are passing values to our arguments by position. It is possible to pass values in two ways - **by position** and **by name**. Each of these function calls are evaluated the same way.

```
cylinder_volume(10, 7)  # pass in arguments by position
cylinder_volume(height=10, radius=7)  # pass in arguments by name
```
