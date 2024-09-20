##Exercise 1: Variable Assignment and Basic Operations
##Create variables to store the following geospatial data:
##
##The latitude and longitude of New York City: 40.7128, -74.0060.
##
##The population of New York City: 8,336,817.
##
##The area of New York City in square kilometers: 783.8.
##
##Perform the following tasks:
##
##Calculate and print the population density of New York City (population per square kilometer).
##
##Print the coordinates in the format “Latitude: [latitude], Longitude: [longitude]”.


ny_lat = 40.7128
ny_long = -74.0060
ny_population = 8336817
ny_areakm2 = 783.8

density_pop = ny_population / ny_areakm2

lat_d = int(ny_lat)
lat_m = (ny_lat - int(ny_lat)) * 60
lat_s = (lat_m - int(lat_m)) * 60

ny_long *= -1

long_d = int(ny_long)
long_m = (ny_long - int(ny_long)) * 60
long_s = (long_m - int(long_m)) * 60
print('-' * 50)
print('Nueva York City')
print('-' * 50)
print('\nPopulation per square kilometer: {0:,.2f}'.format(ny_population / ny_areakm2))
print('Latitud: N {0}° {1:.2f}\' {2:.2f}"'.format(lat_d, lat_m, lat_s))
print('Longitud: W {0}° {1:.2f}\' {2:.2f}"'.format(long_d, long_m, long_s))
print('-' * 50)
