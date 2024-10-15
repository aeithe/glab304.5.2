clothing= ['socks', 'pants', 'shirt', 'polo']
clothing.append("skirt")
print(clothing)

clothing.insert(2,['suit jacket', 'suit pants', 'tie', 'button down'])
print(clothing)

nums= [2, 150, 14, 36, 78, 81, 14, 1000, 54, 14, 14]
print(nums.count(14))

print(sum(nums))


animals= ["koala", "cat", "fox", "panda", "chipmunk", "sloth"]
for animal in animals:
    print(animal)

random_things= ['hello', ['breakfast', 'you', 'pencil', 2], 22, ['burrito', 'taco'],
                [22, 'win', 33, [5], 'laptop']]

def jessSorting(list_to_sort):

    new_list = []

    for item in list_to_sort:
        if type(item) is list:
            if len(item) > 3:
                new_list.append(item[1])

    
    return new_list


list2 = jessSorting(random_things)
print(list2)