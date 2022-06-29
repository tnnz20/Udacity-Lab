username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."

message = username + " accessed the site " + url + " at " + timestamp + "."
print(message)

# Or

list_messages = [username, url, timestamp]
text = ''
for message in list_messages:
    if message == list_messages[0]:
        text += message + " accessed the site "
    elif message == list_messages[-1]:
        text += ' at ' + message + '.'
    else:
        text += message

print(text)

# Quiz: len()
# Use string concatenation and the len() function 
# to find the length of a certain movie star's actual full name. 
# Store that length in the name_length variable. 
# Don't forget that there are spaces in between the different parts of a name!

given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

#todo: calculate how long this name is
name_length = len(given_name + " " + middle_names + " " + family_name)

# Or 

name_length = len(given_name + middle_names + family_name) + 2

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)