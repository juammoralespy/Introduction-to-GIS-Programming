##Exercise 4: Using Tuples
##Create a tuple to store the coordinates (latitude, longitude) of the Eiffel Tower: (48.8584, 2.2945). Perform the following tasks:
##
##Access and print the latitude and longitude values from the tuple.
##
##Try to change the latitude value to 48.8585. What happens? Explain why.


eiffel = (48.8584,2.2945)

print('Eiffel coordinates: Latitude = {} Longitude {}'.format(eiffel[0], eiffel[1]))

eiffel[0] = 48.8585


#The error is because tuples are immutable
