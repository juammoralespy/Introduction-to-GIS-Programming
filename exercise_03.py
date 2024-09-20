##Exercise 3: Using Lists
##Create a list of tuples, where each tuple contains the name of a city and its corresponding latitude and longitude:
##
##New York City: (40.7128, -74.0060)
##
##Los Angeles: (34.0522, -118.2437)
##
##Chicago: (41.8781, -87.6298)
##
##Perform the following tasks:
##
##Add a new city (e.g., Miami: (25.7617, -80.1918)) to the list.
##
##Print the entire list of cities.
##
##Slice the list to print only the first two cities.


ciudades = [('New York City',34.0522,-74.0060),('Los Angeles',34.0522,-118.2437),('Chicago',41.8781,-876298)]

ciudades.append(('Miami',25.7617,-80.1918))

print(ciudades)

print(ciudades[:2])


