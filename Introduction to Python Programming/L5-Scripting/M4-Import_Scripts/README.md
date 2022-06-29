# Importing Local Scripts

We can actually import Python code from other scripts, which is helpful if you are working on a bigger project where you want to organize your code into multiple files and reuse code in those files. If the Python script you want to import is in the same directory as your current script, you just type `import` followed by the name of the file, without the .py extension.

```
import useful_functions
```

It's the standard convention for `import` statements to be written at the top of a Python script, each one on a separate line. This `import` statement creates a **module** object called `useful_functions`. Modules are just Python files that contain definitions and statements. To access objects from an imported module, you need to use dot notation.

```
import useful_functions
useful_functions.add_five([1, 2, 3, 4])
```

We can add an alias to an imported module to reference it with a different name.

```
import useful_functions as uf
uf.add_five([1, 2, 3, 4])
```

## Using a main block

To avoid running executable statements in a script when it's imported as a module in another script, include these lines in an if `__name__` == `"__main__"` block. Or alternatively, include them in a function called main() and call this in the if main block.

Whenever we run a script like this, Python actually sets a special built-in variable called `__name__` for any module. When we run a script, Python recognizes this module as the main program, and sets the `__name__` variable for this module to the string `"__main__"`. For any modules that are imported in this script, this built-in `__name__` variable is just set to the name of that module. Therefore, the condition if `__name__` == `"__main__"` is just checking whether this module is the main program.

## The Standard Library

You can discover new modules at the [Python Module of the Week](https://pymotw.com/3/) blog.

## Usefull Library

- **csv**: very convenient for reading and writing csv files
- **collections**: useful extensions of the usual data types including `OrderedDict`, `defaultdict` and `namedtuple`
- **random**: generates pseudo-random numbers, shuffles sequences randomly and chooses random items
- **string**: more functions on strings. This module also contains useful collections of letters like string.digits (a string containing all characters which are valid digits).
- **re**: pattern-matching in strings via regular expressions
- **math**: some standard mathematical functions
- **os**: interacting with operating systems
- **os.path**: submodule of `os` for manipulating path names
- **sys**: work directly with the Python interpreter
- **json**: good for reading and writing json files (good for web work)

## Techniques for Importing Modules

There are other variants of `import` statements that are useful in different situations.

1. To import an individual function or class from a module:

```
from module_name import object_name
```

2. To import multiple individual objects from a module:

```
from module_name import first_object, second_object
```

3. To rename a module:

```
import module_name as new_name
```

4. To import an object from a module and rename it:

```
from module_name import object_name as new_name
```

5. To import every object individually from a module (DO NOT DO THIS):

```
from module_name import *
```

6. If you really want to use all of the objects from a module, use the standard import module_name statement instead and access each of the objects with the dot notation.

```
import module_name
```

## Modules, Packages, and Names

In order to manage the code better, modules in the Python Standard Library are split down into sub-modules that are contained within a package. A **package** is simply a module that contains sub-modules. A sub-module is specified with the usual dot notation.

Modules that are submodules are specified by the package name and then the submodule name separated by a dot. You can import the submodule like this.

```
import package_name.submodule_name
```
