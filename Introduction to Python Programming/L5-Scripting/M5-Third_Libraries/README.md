# Third-Party Libraries

There are tens of thousands of third-party libraries written by independent developers! You can install them using pip, a package manager that is included with Python 3. pip is the standard package manager for Python, but it isn't the only one. One popular alternative is Anaconda which is designed specifically for data science.

To install a package using pip, just enter "pip install" followed by the name of the package in your command line like this: `pip install package_name`. This downloads and installs the package so that it's available to import in your programs. Once installed, you can import third-party packages using the same syntax used to import from the standard library.

## Using a `requirements.txt` File

Larger Python programs might depend on dozens of third party packages. To make it easier to share these programs, programmers often list a project's dependencies in a file called requirements.txt. This is an example of a requirements.txt file.

```
beautifulsoup4==4.5.1
bs4==0.0.1
pytz==2016.7
requests==2.11.1
```

Each line of the file includes the name of a package and its version number. The version number is optional, but it usually should be included. Libraries can change subtly, or dramatically, between versions, so it's important to use the same library versions that the program's author used when they wrote the program.

You can use pip to install all of a project's dependencies at once by typing `pip install -r requirements.txt` in your command line.

## Useful Third-Party Packages

Being able to install and import third party libraries is useful, but to be an effective programmer you also need to know what libraries are available for you to use. People typically learn about useful new libraries from online recommendations or from colleagues. If you're a new Python programmer you may not have many colleagues, so to get you started here's a list of packages that are popular with engineers at Udacity.

- [IPython](https://ipython.org/) - A better interactive Python interpreter
- [requests](http://docs.python-requests.org/) - Provides easy to use methods to make web requests. Useful for accessing web APIs.
- [Flask](https://flask.palletsprojects.com/en/2.1.x/) - a lightweight framework for making web applications and APIs.
- [Django](https://www.djangoproject.com/) - A more featureful framework for making web applications. Django is particularly good for designing complex, content heavy, web applications.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) - Used to parse HTML and extract information from it. Great for web scraping.
- [pytest](https://docs.pytest.org/en/7.1.x/) - extends Python's builtin assertions and unittest module.
- [PyYAML](https://pyyaml.org/wiki/PyYAML) - For reading and writing [YAML](https://en.wikipedia.org/wiki/YAML) files.
- [NumPy](https://numpy.org/) - The fundamental package for scientific computing with Python. It contains among other things a powerful N-dimensional array object and useful linear algebra capabilities.
- [pandas](https://pandas.pydata.org/) - A library containing high-performance, data structures and data analysis tools. In particular, pandas provides dataframes!
- [matplotlib](https://matplotlib.org/) - a 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments.
- [ggplot](https://ggplot2.tidyverse.org/reference/ggplot.html) - Another 2D plotting library, based on R's ggplot2 library.
- [Pillow](https://python-pillow.org/) - The Python Imaging Library adds image processing capabilities to your Python interpreter.
- [pyglet](https://pyglet.org/) - A cross-platform application framework intended for game development.
- [Pygame](https://www.pygame.org/news) - A set of Python modules designed for writing games.
- [pytz](http://pytz.sourceforge.net/) - World Timezone Definitions for Python
