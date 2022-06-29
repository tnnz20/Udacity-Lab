verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)
print()
# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!

# Answer 1
print("Verse has a length of {} characters.".format(len(verse)))

# Answer 2
print("The first occurence of the word 'and' occurs at the {}th index.".format(verse.find('and')))

# Answer 3
print("The last occurence of the word 'you' occurs at the {}th index.".format(verse.rfind('you')))

# Answer 4
print("The word 'you' occurs {} times in the verse.".format(verse.count('you')))
