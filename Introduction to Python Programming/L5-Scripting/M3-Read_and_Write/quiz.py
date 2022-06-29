def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for line in f:
            name = line.split(",")[0]
            cast_list.append(name)

    return cast_list

cast_list = create_cast_list('L5-Scripting/M3-Read_and_Write/flying_circus_cast.txt')
for actor in cast_list:
    print(actor)