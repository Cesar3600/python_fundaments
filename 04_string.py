name = "Delia"
last_name = "Alva Lopez"
print(name)
print(last_name)

full_name = name + " " + last_name
print(full_name)

quotes = "I'am Cesar"
print(quotes)

quotes2 = ' She said "Hello" '
print(quotes2)

#format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print(template)

template = "Hola, mi nombre es {} y mis apellidos son {}".format(name,last_name);
print(template)

template = f"Hola, Soy {name} y mis apellidos son {last_name}"
print(template)
