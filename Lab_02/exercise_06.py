##Exercise 6: Using For Loops to Process Coordinate Lists
##Create a list of tuples representing coordinates (latitude, longitude).
##
##Write a for loop that prints each coordinate and indicates whether it is in the Northern
#or Southern Hemisphere based on the latitude.

america_capitals = [(45.37,-75.65),(38.89,-76.95),(19.43,-99.13),(18.53,-72.34),(18.4,-66.08),(18.02,-76.8),(14.62,-90.52),(14.1,-87.2),(13.7,-89.2),(12.15,-86.27),(10.5,-66.9),(9.93,-84.08),(4.93,-52.33),(4.63,-74.08),(-0.23,-78.52),(-15.79,-47.9),(-16.5,-68.15),(-33.48,-70.65),(-34.67,-58.41),(17.13,-88.48),(22.91,-81.88),(9.22,-79.41),(19.22,-70.3),(5.94,-58.77),(4.84,-55.17),(-34.03,-55.94),(-12.07,-76.74),(-25.23,-57.49)]

for dd in america_capitals:
    if dd[0] > 0:
        print('Hemisphere Northern: ',dd)
    else:
        print('Hemisphere Southern: ',dd)
