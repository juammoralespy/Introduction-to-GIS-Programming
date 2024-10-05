##Exercise 1: Calculating Distances with Functions
##Define a function calculate_distance that takes two geographic coordinates
#(latitude and longitude) and returns the distance between them using the Haversine formula.
##
##Use this function to calculate the distance between multiple pairs of coordinates.

import math

# Python 3 program for the
# haversine formula
def calculate_distance(lat1, lon1, lat2, lon2):
	
	# distance between latitudes
	# and longitudes
	dLat = (lat2 - lat1) * math.pi / 180.0
	dLon = (lon2 - lon1) * math.pi / 180.0

	# convert to radians
	lat1 = (lat1) * math.pi / 180.0
	lat2 = (lat2) * math.pi / 180.0

	# apply formulae
	a = (pow(math.sin(dLat / 2), 2) +
		pow(math.sin(dLon / 2), 2) *
			math.cos(lat1) * math.cos(lat2));
	rad = 6371
	c = 2 * math.asin(math.sqrt(a))
	return rad * c



coordinates = [[(37.7849,-122.4195),(37.78477,-122.4212)],[(37.78477,-122.4212),(37.7856,-122.4213)]]

for i in coordinates:
	print(i)
		
	print('distancia: {0:.2f}'.format(calculate_distance(i[0][0], i[0][1], i[1][0], i[1][1])))
