# 6-1/6-3. Person information and information printed. (This exercise encompasses all three exercise.)

# below variables prompts input request which is then stored in variable
fname = input("fname > ")
lname = input("lname > ")
age = input("age > ")
city = input("city > ")

# stylised printing
print("\n++++++++++++++++++++++++\n")

# dictionary assigned to person var

person = {'first_name': fname, 'last_name': lname, 'age': age, 'city': city}  # <- value of dict keys = inputted vars

# for looping over key value pair in dict and printing in stylised manner.
for k, v in person.items():
    print(k + ':', v)

# stylised printing
print("\n++++++++++++++++++++++++\n")

# individual value printing.
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])


