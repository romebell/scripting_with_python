# open a file
rome_file = open('rome.txt', 'a')

numbers = [1,2,3]
for i in range(len(numbers)):
    num = numbers[i]
    rome_file.write("{}\n".format(num))

# write to the file
# rome_file.write('\nHello\n')
# close a file
rome_file.close()

# read a file
# print(rome_file.read())

# If file is not found, one will be created
adam_file = open('adam.txt', 'w')
adam_file.write('Adam')
# adam_file.write('Adam')
adam_file.close()


# Look up how to read lines from a file in python
new_file = open('new_file.txt')
file_items = new_file.readlines()

for i in range(len(file_items)):
    each_item = file_items[i]
    print('Before: {}'.format(each_item))
    print(each_item[0:-1])
    file_items[i] = each_item[0:-1]
    print(file_items)

# print(file_items)

new_file.close()

# Problem:
# Make a new file called 713_list.py and iterate through the squad_713 list and write each person in the list to a file called general_assembly.txt .
# Create the general_assembly.txt file using python.
# Be sure to put each person on their own line using \n .
# commit your changes and push to Github
# squad_713 list below:

squad_713 = [
    'Alice',
    'Alpha',
    'Anthony',
    'Barent',
    'Branden',
    'Channee',
    'Cristina',
    'Cabassa',
    'Elaine',
    'Han',
    'Irene',
    'Joshua',
    'Levin',
    'Lizz',
    'Margaret',
    'Nicholas',
    'Philip',
    'Rohun',
    'Sameh',
    'Shane',
    'Steven',
    'Subrata',
    'Tanner',
    'Yoel',
    'Adam',
    'Pete',
    'Rome',
    'Taylor'
]

ga_file = open('general_assembly.txt', 'w')

for i in range(len(squad_713)):
    person = squad_713[i]

    ga_file.write('{}\n'.format(person))

ga_file.close()