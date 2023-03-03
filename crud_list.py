letters = ['A', 'B', 'C', 'D', 'E', 'F']

# Escribe tu solución 👇

letters.append('G')
print(letters)
letters[0] = 'Z'
print(letters)
index = letters.index('C')
letters.pop(index)
print(letters)
letters.reverse()
print(letters)


letters.append('G')
letters[0] = 'Z'
index = letters.index('C')
letters.pop(index)
letters.reverse()
