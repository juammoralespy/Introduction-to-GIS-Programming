##Exercise 1: Manipulating Geographic Location Strings
##Create a string that represents the name of a geographic feature (e.g., "Amazon River").
##
##Convert the string to lowercase and then to uppercase.
##
##Concatenate the string with the name of the country (e.g., "Brazil") to create a full location name.
##
##Repeat the string three times, separating each repetition with a dash (-).

feature_geographic = 'Amazon River'

print(feature_geographic)

feature_geographic = feature_geographic.lower()

print(feature_geographic)

feature_geographic = feature_geographic.upper()

print(feature_geographic)

feature_geographic = feature_geographic + ' Brazil '

print(feature_geographic)

print((feature_geographic + '- ') * 3)
