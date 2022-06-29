# Practice

from lib2to3.pgen2 import token


sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

# Write a for loop to print out each word in the sentence list, one word per line

for word in sentence:
    print(word)
# Write a for loop using range() to print out multiples of 5 up to 30 inclusive

for i in range(5,35,5):
    print(i)


# Quiz: Create Usernames

# Write a for loop that iterates over the names list to create a usernames list. 
# To create a username for each name, make everything lowercase and replace spaces 
# with underscores. Running your for loop over the list:
# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
# should create the list:
# usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here

for name in names:
    name = name.replace(' ','_').lower()
    usernames.append(name)
print(usernames)

# Quiz: Modify Usernames with Range

# Write a for loop that uses range() to iterate over the positions in usernames to modify the list. Like you did in the previous quiz, change each name to be lowercase and replace spaces with underscores. After running your loop, this list

# usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# should change to this:

# usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here

for i in range(len(usernames)):
    usernames[i] = usernames[i].replace(' ', '_').lower()
print(usernames)

# Quiz: Tag Counter

# Write a for loop that iterates over a list of strings, tokens, 
# and counts how many of them are XML tags. XML is a data language similar to HTML. 
# You can tell if a string is an XML tag if it begins with a left angle bracket "<" 
# and ends with a right angle bracket ">". Keep track of the number of tags using 
# the variable count.

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here

# for i in tokens:
#     if '<' in i or '>' in i:
#         count +=1
#     else:
#         pass

for i in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1
    else:
        pass
print(count)

# Quiz: Create an HTML List
# Write some code, including a for loop, that iterates over a list of strings 
# and creates a single string, html_str, which is an HTML list. For example, 
# if the list is items = ['first string', 'second string'], printing 
# html_str should output:

# <ul>
# <li>first string</li>
# <li>second string</li>
# </ul>

items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
for i in items:
    html_str += '<li>' + i + '</li>\n'

html_str += '</ul>'
print(html_str)