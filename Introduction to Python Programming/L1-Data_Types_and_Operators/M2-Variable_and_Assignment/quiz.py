# Quiz: Assign and Modify Variables
print('\nQuiz: Assign and Modify Variables\n')
# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
print(f'First reservoir_volume {reservoir_volume}')
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6
print(f'First rainfall {rainfall}')

# decrease the rainfall variable by 10% to account for runoff
rainfall *= .9
print(f'Decrease {rainfall}')

# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall
print(f'Add reservoir_volume with rainfall{reservoir_volume}')

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume *=  1.05
print(f'Increase reservoir_volume by 5% {reservoir_volume}')

# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume *= 0.95
print(f'Decrease reservoir_volume by 5% {reservoir_volume}')

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5
print(f'reservoir_volume - 2.5e5 {reservoir_volume}')

# print the new value of the reservoir_volume variable
print(reservoir_volume)

# Quiz: Changing Variable Values
print('\nQuiz: Changing Variable Value\n')
carrots = 24
rabbits = 8
crs_per_rab = carrots/rabbits
rabbits = 12
print(crs_per_rab)
