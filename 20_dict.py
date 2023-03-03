
#insercion y actualizacion
person = {
    'name':'nico',
    'last_name':'molina',
    'langs':['python','javascript'],
    'age':99
}

print(person)

person['name'] = 'Santi'
print(person)

person['age'] -= 50
print(person)

person['langs'].append('Rust')
print(person)


del person['age']
print(person)

person.pop('last_name')
print(person)

print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())


