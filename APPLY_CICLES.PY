import random

print('*'*33)
print('stone, paper, scissor game'.upper())
print('*'*33)

user_points = 0
pc_points = 0
options = ('piedra','papel','tijera')

while True:
  print('%'*33)
  print(f'puntos de usuario:{user_points}')
  print(f'puntos de usuario:{pc_points}')

  #insert options
  user_option = input('Insert a option:').lower()

  #VERIFICAR SI OPCION ES VALIDA
  valid = user_option in options
  if valid:
    print("valid -> ",valid)
    pc_option = random.choice(options)

    if user_points == 3:
        print('ganaste!!!!!!!!!!!!!!!!'.upper())
        break

    if pc_option == 3:
        print('gano la pc'.upper())
        break

    if pc_option == user_option:
      print('no hay punto, empate!')

    elif(pc_option == 'piedra'):
      if(user_option =='papel'):
        print('Papel vence a piedra')
        print('Ganaste un punto')
        user_points += 1
      else:
        print('Piedra vence a tijera')
        print('La computadora gano un punto')
        pc_points += 1

    elif(pc_option == 'papel'):
      if(user_option =='piedra'):
        print('Papel vence a piedra')
        print('La computadora gano un punto')
        pc_points += 1
      else:
        print('Tijera vence piedra')
        print('Ganaste un punto')
        user_points += 1

    elif(pc_option == 'tijera'):
      if(user_option =='papel'):
        print('tijera vence a papel')
        print('La computadora gano un punto')
        pc_points += 1
      else:
        print('Piedra vence a tijera')
        print('Ganaste un punto')
        user_points += 1

  else:
    print('ingresa una opcion valida!')

