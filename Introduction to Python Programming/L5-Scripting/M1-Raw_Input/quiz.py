# Quiz: Generate Messages
# Write a script that does the following:

# Ask for user input 3 times. Once for a list of names, once 
# for a list of missing assignment counts, and once for a list of grades. 
# Use this input to create lists for names, assignments, and grades.

# Use a loop to print the message for each student with the correct values. 
# The potential grade is simply the current grade added to two times 
# the number of missing assignments.

names = input('Enter names separated by commas : ').title().split(',')
assignments = input('Enter assignment counts separated by commas : ').split(',')
grades = input('Enter grades separated by commas : ').split(',')


message = "\nHi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names,assignments,grades):
    probablity_grade = int(grade) + (int(assignment)*2)
    print(message.format(name, assignment, grade, probablity_grade))
