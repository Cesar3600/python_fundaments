import random

options = ('piedra','papel','tijera')

user_option = input('Piedra, papel o tijera :::=> ').lower()
computer_option = random.choices(options)

print('user option => ', user_option)
print('computer option => ', computer_option)

if not user_option in options:
  print('no es una opcion valida')


if user_option == computer_option:
    print("Draw!")
elif user_option == 'papel':
    if computer_option =='piedra':
      print('papel gana a piedra')
      print('Win!')
    else:
      print('tijera gana a papel')
      print('Lose!')    
elif user_option =='tijera':
  if computer_option =='piedra': 
    print('piedra gana a tijera')
    print('Lose!')
  else:
    print('Tijera gana a papel')
    print('Win!')
elif user_option =='piedra':
  if computer_option =='tijera': 
    print('piedra gana a Tijera')
    print('Win!')
  else:
    print('Papel gana a piedra')
    print('Lose!')

