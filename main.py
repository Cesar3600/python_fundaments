user_option = input('Piedra, papel o tijera :::=> ')
computer_option = 'tijera'

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

