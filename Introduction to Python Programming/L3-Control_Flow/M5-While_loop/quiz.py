# Practice: Factorials with While Loops
# Find the factorial of a number using a while loop.

# A factorial of a whole number is that number multiplied 
# by every whole number between itself and 1. For example, 
# 6 factorial (written "6!") equals 6 x 5 x 4 x 3 x 2 x 1 = 720. So 6! = 720.

# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while current <= number:
    # multiply the product so far by the current number
    product *= current
    
    # increment current with each iteration until it reaches number
    current += 1

# print the factorial of number
print(product)

# Practice: Factorials with For Loops
# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

for num in range(2, number+1):
    product *= num

# print the factorial of number
print(product)

# Quiz: Count By

# Suppose you want to count from some number start_num by another number
# count_by until you hit a final number end_num. Use break_num as the variable 
# that you'll change each time through the loop. For simplicity, assume that 
# end_num is always larger than start_num and count_by is always positive.

# Before the loop, what do you want to set break_num equal to? 
# How do you want to change break_num each time through the loop? 
# What condition will you use to see when it's time to stop looping?

# After the loop is done, print out break_num, showing the value 
# that indicated it was time to stop looping. It is the case that 
# break_num should be a number that is the first number larger than end_num.

start_num = 5
end_num = 100
count_by = 2

break_num = start_num
# write a while loop that uses break_num as the ongoing number to
while break_num < end_num:
#   check against end_num
    break_num += count_by


print(break_num)

# Quiz: Count By Check
# Suppose you want to count from some number start_num by another number 
# count_by until you hit a final number end_num, and calculate break_num 
# the way you did in the last quiz.

# Now in addition, address what would happen if someone gives a start_num 
# that is greater than end_num. If this is the case, set result to 
# "Oops! Looks like your start value is greater than the end value. Please try again." 
# Otherwise, set result to the value of break_num.

start_num = 5
end_num = 100
count_by = 5

# write a condition to check that end_num is larger than start_num before looping
if start_num < end_num:
    break_num = start_num
# write a while loop that uses break_num as the ongoing number to 
    while break_num < end_num:
#   check against end_num
        break_num += count_by
        result = break_num
else:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."


print(result)

# Quiz: Nearest Square
# Write a while loop that finds the largest square number less than an 
# integerlimit and stores it in a variable nearest_square. A square number 
# is the product of an integer multiplied by itself, for example 36 is a 
# square number because it equals 6*6.

# For example, if limit is 40, your code should set the nearest_square to 36.
limit = 40

# write your while loop here
num = 0
while (num+1)**2 < limit:
    num +=1
nearest_square = (num)**2

print(nearest_square)

# Find 5 odd number from list

num_list = [
    422, 136, 524, 85, 96, 719, 
    85, 92, 10, 17, 312, 542, 
    87, 23, 86, 191, 116, 35, 
    173, 45, 149, 59, 84, 69, 
    113, 166
    ]

count_odd = 0
list_sum = 0
i = 0
len_num_list = len(num_list)

while (count_odd < 5) and (i < len_num_list): 
    if num_list[i] % 2 == 1:
        list_sum += num_list[i]
        count_odd += 1
    i += 1

print ("The numbers of odd numbers added are: {}".format(count_odd))
print ("The sum of the odd numbers added is: {}".format(list_sum))