
person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}

person['twitter'] = '@nicobytes'
person['name'] = 'Felipe'

del person['age']

print(list(person.keys()))
print(list(person.values()))
print(person)


