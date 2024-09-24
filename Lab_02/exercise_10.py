##Exercise 10: Generating and Analyzing Random Coordinates
##Write a program that generates random coordinates (latitude and longitude between -180 and 180 degrees).
##
##Use a while loop to keep generating coordinates until a pair with both latitude and longitude greater than 50 is generated.
##
##Print each generated coordinate and the final coordinate that meets the condition.

    
import random

next_step = True
print()
while next_step:
    latitude = random.randint(-180,180)
    longitude = random.randint(-180,180)
    
    if latitude > 50 and longitude > 50:
        next_step = False
    else:
        print(latitude,',',longitude)

print('latitude and longitude greater than 50: {},{}'.format(latitude,longitude))

