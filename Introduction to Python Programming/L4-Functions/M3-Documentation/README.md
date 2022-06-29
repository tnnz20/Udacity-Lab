# Documentation

Documentation is used to make your code easier to understand and use. Functions are especially readable because they often use documentation strings, or docstrings. Docstrings are a type of comment used to explain the purpose of a function, and how it should be used. Here's a function for population density with a docstring.

```
def population_density(population, land_area):
    """Calculate the population density of an area. """
    return population / land_area
```

Docstrings are surrounded by triple quotes. The first line of the docstring is a brief explanation of the function's purpose. If you feel that this is sufficient documentation you can end the docstring at this point; single line docstrings are perfectly acceptable, as in the example above.

```
def population_density(population, land_area):
    """Calculate the population density of an area.

    INPUT:
    population: int. The population of that area
    land_area: int or float. This function is unit-agnostic, if you pass in values in terms
    of square km or square miles the function will return a density in those units.

    OUTPUT:
    population_density: population / land_area. The population density of a particular area.
    """
    return population / land_area
```

If you think that a longer description would be appropriate for the function, you can add more information after the one-line summary. In the example above, you can see that we wrote an explanation of the function's arguments, stating the purpose and types of each one. It's also common to provide some description of the function's output.

Every piece of the docstring is optional, however, docstrings are a part of good coding practice. You can read more about docstring conventions [here](https://peps.python.org/pep-0257/).

> Example 1

```
def readable_timedelta(days):
    """Return a string of the number of weeks and days included in days."""
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)
```

> Example 2

```
def readable_timedelta(days):
    """Return a string of the number of weeks and days included in days.

    Args:
        days (int): number of days to convert
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)
```

> Example 3

```
def readable_timedelta(days):
    """
    Return a string of the number of weeks and days included in days.

    Parameters:
    days -- number of days to convert (int)

    Returns:
    string of the number of weeks and days included in days
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)
```
