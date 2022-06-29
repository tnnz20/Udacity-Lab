# Variables and Assignment Operators

## Variables

Variables are used all the time in Python! Below is the example you saw in the video where we performed the following:

```
mv_population = 74728
```

Here `mv_population` is a variable, which holds the value of `74728`. This assigns the item on the right to the name on the left, which is actually a little different than mathematical equality, as `74728` does not hold the value of `mv_population`.

In any case, whatever term is on the `left side`, is now a name for whatever value is on the `right side`. Once a value has been assigned to a variable name, you can access the value from the variable name.

> Normal Assignment

```
x = 3
y = 4
z = 5
```

> Multiple Assignment

```
x, y, z = 3, 4, 5
```

Besides writing variable names that are descriptive, there are a few things to watch out for when naming variables in Python.

1. Only use ordinary letters, numbers and underscores in your variable names. They can’t have spaces, and need to start with a letter or underscore.

2. You can’t use Python's reserved words, or "keywords," as variable names. There are reserved words in every programming language that have important purposes, and you’ll learn about some of these throughout this course. Creating names that are descriptive of the values often will help you avoid using any of these keywords. Here you can see a [table of Python's reserved words](https://docs.python.org/3/reference/lexical_analysis.html#keywords).

3. The pythonic way to name variables is to use all lowercase letters and underscores to separate words.

### Example naming variable :

> Good

```
my_height = 58
my_lat = 40
my_long = 105
```

> Bad

```
my height = 58
MYLONG = 40
MyLat = 105
```

## Assignment Operators

Below are the assignment operators from the video. You can also use \*= in a similar way, but this is less common than the operations shown below. You can find some practice with much of what we have already covered here.

![Udacity](https://video.udacity-data.com/topher/2018/January/5a7118b3_screen-shot-2018-01-30-at-5.14.39-pm/screen-shot-2018-01-30-at-5.14.39-pm.png)

### Example Assignment Operator

> Without Assignment Operator

```
mv_population = 74728
mv_population = 74728 + 4000 - 600
print(mv_population) # 78128
```

> With Assignment Operator

```
mv_population = 74728
mv_population += 4000 - 600
print(mv_population) # 78128
```

## Solution: Changing Variables

For the first multiple choice quiz, the correct answer is that the value of crs_per_rab has not changed. That is, it is still 3.0.

This is because when a variable is assigned, it is assigned to the value of the expression on the right-hand-side, not to the expression itself. In the line:

```
>>> crs_per_rab = carrots/rabbits
```

Python actually did the calculation to evaluate the expression on the right-hand-side, carrots/rabbits, and then assigned the variable crs_per_rab to be the value of that expression. It promptly forgot the formula, only saving the result in the variable.

In order to update the value of crs_per_rab to take into account the change in rabbits, we need to run this line again:

```
>>> crs_per_rab = carrots/rabbits
>>> print(crs_per_rab)
2.0
```

That’s the new number of carrots per rabbit after the increase in the number of rabbits. All of our variables have been updated to take this into account.

## Supporting Materials

[Scientifc Notation](https://en.wikipedia.org/wiki/Scientific_notation)
