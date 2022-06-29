# Reading and Writing Files

## Reading a File

```
f = open('my_path/my_file.txt', 'r')
file_data = f.read()
f.close()
```

1. First open the file using the built-in function, `open`. This requires a string that shows the path to the file. The `open` function returns a file object, which is a Python object through which Python interacts with the file itself. Here, we assign this object to the variable `f`.
2. There are optional parameters you can specify in the `open` function. One is the mode in which we open the file. Here, we use `r` or read only. This is actually the default value for the mode argument.
3. Use the `read` method to access the contents from the file object. This `read` method takes the text contained in a file and puts it into a string. Here, we assign the string returned from this method into the variable `file_data`.
4. When finished with the file, use the `close` method to free up any system resources taken up by the file.

## Writing to a File

```
f = open('my_path/my_file.txt', 'w')
f.write("Hello there!")
f.close()
```

1. Open the file in writing ('w') mode. If the file does not exist, Python will create it for you. If you open an existing file in writing mode, any content that it had contained previously will be deleted. If you're interested in adding to an existing file, without deleting its content, you should use the append ('a') mode instead of write.
2. Use the write method to add text to the file.
3. Close the file when finished.

## Too Many Open Files

Run the following script in Python to see what happens when you open too many files without closing them!

```
files = []
for i in range(10000):
    files.append(open('some_file.txt', 'r'))
    print(i)
```

> Output

```
Error
```

## With

Python provides a special syntax that auto-closes a file for you once you're finished using it.

```
with open('my_path/my_file.txt', 'r') as f:
    file_data = f.read()
```

This `with` keyword allows you to open a file, do operations on it, and automatically close it after the indented code is executed, in this case, reading from the file. Now, we don’t have to call f.close()! You can only access the file object, f, within this indented block.

## List file methods

| **Method**   | **Description**                                                                      |
| ------------ | ------------------------------------------------------------------------------------ |
| close()      | Closes the file                                                                      |
| detach()     | Returns the separated raw stream from the buffer                                     |
| fileno()     | Returns a number that represents the stream, from the operating system's perspective |
| flush()      | Flushes the internal buffer                                                          |
| isatty()     | Returns whether the file stream is interactive or not                                |
| read()       | Returns the file content                                                             |
| readable()   | Returns whether the file stream can be read or not                                   |
| readline()   | Returns one line from the file                                                       |
| readlines()  | Returns a list of lines from the file                                                |
| seek()       | Change the file position                                                             |
| seekable()   | Returns whether the file allows us to change the file position                       |
| tell()       | Returns the current file position                                                    |
| truncate()   | Resizes the file to a specified size                                                 |
| writable()   | Returns whether the file can be written to or not                                    |
| write()      | Writes the specified string to the file                                              |
| writelines() | Writes a list of strings to the file                                                 |

## File Handling

`"r"` - Read - Default value. Opens a file for reading, error if the file does not exist

`"a"` - Append - Opens a file for appending, creates the file if it does not exist

`"w"` - Write - Opens a file for writing, creates the file if it does not exist

`"x"` - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

`"t"` - Text - Default value. Text mode

`"b"` - Binary - Binary mode (e.g. images)
