'''
for element in range(1,21):
    print(element)

my_list = [23,45,67,89,43]

for element in my_list:
    print(element)

my_tuple = ('nico','july','santy')

for element in my_tuple:
  print(element)
'''


product = {
   'name' : 'Camisa',
   'price' : 100,
   'stock' : 99
}

for key in product:
  print(key, '=>', product[key])


for key,value in product.items():
  print(key,'=>',value)


people = [
  {
    'name':'Cesar',
    'age': 46
  },
  {
    'name':'Delia',
    'age': 30
  },
  {
    'name':'Mikaela',
    'age': 1
  },
]

for person in people:
  print('name =>', person['name'])


