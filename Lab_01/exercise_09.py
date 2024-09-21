##Exercise 9: Dictionary Operations
##Using the dictionary from Exercise 6, perform the following tasks:
##
##Check if the key “Length” exists in the dictionary.
##
##Print all the keys in the dictionary.
##
##Print all the values in the dictionary.

rios = {'Name':'Amazon River','Length':'6400 km', 'Countries':['Brazil','Peru','Colombia']}


print('\nVerifica clave Length: ',rios.get('Length'))

print()

for k in rios.keys():
    print(k)

print()

for v in rios.values():
    print(v)
