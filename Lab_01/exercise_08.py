##Exercise 8: List Operations
##Given the list of cities from Exercise 3, perform the following operations:
##
##Sort the list of cities alphabetically by name.
##
##Create a new list that contains only the city names.
##
##Remove the last city from the original list and print the updated list.


ciudades = [('New York City',34.0522,-74.0060),('Los Angeles',34.0522,-118.2437),('Chicago',41.8781,-876298)]

print(ciudades)

ciudades.sort()

print(ciudades)

##ciudades2 = list((x for x in ciudades[0][:1]))

ciudades2 = []

for x in ciudades:
    ciudades2.append(x[0])

print(ciudades2)

ciudades.pop()

print(ciudades)
