text="Ella sabe Python"
print(text[0])
print(text[1])
# print(text[999])

size = len(text)
print('size => ',size)
print(text[size-1])
print(text[-1])

#slicing
print(text[0:5])
print(text[10:16])

#toma desde el inicio hasta el 10 elemento
print(text[0:10])
print(text[:10])

#toma caracteres desde el final hasta 5
print(text[5:-1])
print(text[5:])


print(text[:])

#el tercer numero se refiere a numeros de saltos
print(text[10:16:1])
print(text[10:16:2])
print(text[::2])