
my_dict = {}
print(type(my_dict))

my_dict = {
    'name':'Catherine',
    'lastName':'Contreras',
    'age':1
}
print(my_dict)

print(len(my_dict))

print(my_dict['name'])
print(my_dict['lastName'])

print(my_dict.get('age'))
print(my_dict.get('name'))
print(my_dict.get('lastName'))

print('avion' in my_dict)
print('name' in my_dict)