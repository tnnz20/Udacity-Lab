# Quiz: Using Truth Values of Objects

"""
If prize is None, result should be set to "Oh dear, no prize this time."
If prize contains a prize name, result should be set to 
"Congratulations! You won a {}!".format(prize). This will avoid having 
the multiple result assignments for different prizes.
"""

points = 160  # use this as input for your submission

# establish the default prize value to None
prize = None

# use the points value to assign prizes to the correct prize names
if points > 0 and points <= 50:
    prize = "wooden rabbit"
elif points >= 151 and points <= 180:
    prize = 'wafer-thin mint'
elif points >= 181 and points <= 200:
    prize = "penguin"
else:
    prize = False

# use the truth value of prize to assign result to the correct prize
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."

print(result)