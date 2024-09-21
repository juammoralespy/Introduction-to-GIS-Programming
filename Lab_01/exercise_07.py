##Exercise 7: Nested Data Structures
##Create a dictionary to represent a city that contains the city’s name, population, and coordinates (latitude, longitude):
##
##Name: “Tokyo”
##
##Population: 13,515,271
##
##Coordinates: (35.6895, 139.6917)
##
##Perform the following tasks:
##
##Access and print the population of the city.
##
##Access and print the city’s latitude.
##
##Update the population to 14,000,000 and print the updated dictionary.


ciudad = {'Name': 'Tokyo', 'Population':'13,515,271', 'Coordinates':(35.6895,139.6917)}

print('Population: ',ciudad['Population'])

print('Latitud: ',ciudad['Coordinates'][0])

ciudad['Population'] = '14,000,000'

print(ciudad)

