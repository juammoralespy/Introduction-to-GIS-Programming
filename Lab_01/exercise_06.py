##Exercise 6: Working with Dictionaries
##Create a dictionary to store information about a specific geospatial feature, such as a river:
##
##Name: “Amazon River”
##
##Length: 6400 km
##
##Countries: [“Brazil”, “Peru”, “Colombia”]
##
##Perform the following tasks:
##
##Add a new key-value pair to the dictionary to store the river’s average discharge (e.g., 209,000 m³/s).
##
##Update the length of the river to 6992 km.
##
##Print the dictionary.


rios = {'Name':'Amazon River','Length':'6400 km', 'Countries':['Brazil','Peru','Colombia']}

print(rios)

rios['Average'] = '209,000 m3/s'

rios['Length'] = '6992 km'

print(rios)
