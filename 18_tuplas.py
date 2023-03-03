
numbers = (1,2,3,5)

print(numbers)
print(type(numbers))


strings = ('nico','zulema','santi')

print(strings)
print(type(strings))

#puedes acceder a la informacion de una tupla 
print('0 =>', numbers[0])
print('-1 =>', numbers[-1])


#crud
#numbers.append(10)
print(numbers)

#numbers[-1] = 'Change'
print(numbers)


print(strings)
print(strings.index('zulema'))


my_list = list(strings)
print(my_list)
print(type(my_list))

my_list[my_list.index('zulema')] = 'Mikaela'
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))
