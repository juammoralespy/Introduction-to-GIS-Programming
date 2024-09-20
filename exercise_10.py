##Exercise 10: Practical Application
##Imagine you have a list of tuples, each representing a location with its name, latitude, and longitude:
##
##locations = [
##    ("Mount Everest", 27.9881, 86.9250),
##    ("K2", 35.8808, 76.5155),
##    ("Kangchenjunga", 27.7025, 88.1475),
##]
##Perform the following tasks:
##
##Create a new list that contains only the names of the locations.
##
##Create a dictionary where the keys are location names and the values are tuples of their coordinates.
##
##Print the latitude of “K2” using the dictionary.

locations = [
    ("Mount Everest", 27.9881, 86.9250),
    ("K2", 35.8808, 76.5155),
    ("Kangchenjunga", 27.7025, 88.1475),
]

locations_name = []

for x in locations:
    locations_name.append(x[0])

print(locations_name)

dict_locations = {}

print()

for x in locations:
    print(x[0])
    print(x[1])
    print(x[2])
    dict_locations[x[0]] = (x[1],x[2])

print()

print(dict_locations)

if 'K2' in dict_locations:
    print('Latitud of K2',dict_locations['K2'][0])
