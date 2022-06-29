# Write your code here
# HINT: create a dictionary from flowers.txt
def create_flowerdict(filename):
    flower_dict = {}
    with open(filename, 'r') as f:
        for line in f:
            key = line.split(': ')[0].lower()
            flower = line.split(': ')[1].strip()
            flower_dict[key] = flower
    return flower_dict

# HINT: create a function to ask for user's first and last name
def main():
    flower_path = 'L5-Scripting/flower.txt'
    flower_d = create_flowerdict(flower_path)

    full_name = input("Enter your First [space] Last name only: ")
    first_name = full_name[0].lower()
    first_letter = first_name[0]
    print("Unique flower name with the first letter: {}".format(flower_d[first_letter]))

# print the desired output
if __name__ == '__main__':
    main()