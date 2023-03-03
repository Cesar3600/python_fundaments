
#CRUD -> Create, read, update, delete
numbers = [1,2,3,4,5]
print(numbers[1])

numbers[-1] =10
print(numbers)


numbers.append(700)
print(numbers)

numbers.insert(0,12)
print(numbers)

numbers.insert(0,'Hola')
print(numbers)


numbers.insert(3,'Change')
print(numbers)


tasks = ['Todo 1', 'Todo 2' , 'Todo 3']
new_list = numbers + tasks
print(new_list)


# para saber la posicion del elemento en una lista
print(new_list.index('Todo 2'))

index = new_list.index('Todo 2')
new_list[index] = 'Todo Changed'
print(new_list)


new_list.remove('Todo 1')
print(new_list)

new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

new_list.reverse()
print(new_list)


numbers_a = [1,4,6,3]
numbers_a.sort()
print(numbers_a)

strings = ['re','ab','ed']
strings.sort()
print(strings)

