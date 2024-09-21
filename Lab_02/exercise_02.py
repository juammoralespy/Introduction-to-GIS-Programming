##Exercise 2: Extracting and Formatting Coordinates
##Given a string with the format "latitude, longitude" (e.g., "40.7128N, 74.0060W"),
##extract the numeric values of latitude and longitude.
##
##Convert these values to floats and remove the directional indicators (N, S, E, W).
##
##Format the coordinates into a POINT WKT string (e.g., "POINT(-74.0060 40.7128)").

coordinates = "40.7128N, 74.0060W"
coordinates = coordinates.upper()

coordinate_identify = coordinates.replace(' ','').split(',')

if 'N' in coordinate_identify[0] or 'S' in coordinate_identify[0]:
    latitude = float(coordinate_identify[0][:-1])
    
if 'W' in coordinate_identify[1] or 'E' in coordinate_identify[1]:
    longitude = float(coordinate_identify[1][:-1])

if 'N' in coordinate_identify[0]:
    latitude2 = float(coordinate_identify[0][:-1])
elif 'S' in coordinate_identify[0]:
    latitude2 = float(coordinate_identify[0][:-1]) * -1

if 'W' in coordinate_identify[1]:
    longitude2 = float(coordinate_identify[1][:-1]) * -1
elif 'E' in coordinate_identify[1]:
    longitude2 = float(coordinate_identify[1][:-1])

print('\nCoordinates: ',coordinates)

print('Latitude: ',latitude2)
print('Longitude: ',longitude2)

wkt_str = '"' + 'POINT(' + str(longitude2) + ',' + str(latitude2) + ')' + '"'

print('WKT: ', wkt_str)
