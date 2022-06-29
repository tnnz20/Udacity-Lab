# Quiz: Extract First Names

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]
print(first_names)

print()

# Quiz: Multiples of Three
multiples_3 = [num*3 for num in range(1,21)]
print(multiples_3)

print()

# Quiz: Filter Names by Scores

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, score in scores.items() if score >= 65]
print(passed)

print()