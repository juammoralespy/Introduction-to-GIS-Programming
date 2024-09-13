# -*- coding: utf-8 -*-
"""Copy of scratchpad

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17npauScZy4T2KL799OTFrBMSLI6hmmdF
"""

num_features = 500  # Represents the number of features in a geospatial dataset

latitude = 35.6895  # Represents the latitude of a point on Earth's surface
longitude = 139.6917  # Represents the longitude of a point on Earth's surface

coordinate_system = "WGS 84"  # Represents a commonly used coordinate system

is_georeferenced = True  # Represents whether a dataset is georeferenced or not

coordinates = [
    35.6895,
    139.6917,
]  # A list representing latitude and longitude of a point

feature_attributes = {
    "name": "Mount Fuji",
    "height_meters": 3776,
    "type": "Stratovolcano",
    "location": [35.3606, 138.7274],
}

print("Hello World!\nThis is a Python script.")

num_features += 20
print("Updated number of features:", num_features)

import math

latitude = 35.6895
latitude_radians = math.radians(latitude)
print("Latitude in radians:", latitude_radians)

coordinates = [35.6895, 139.6917]
coordinates.append(34.0522)  # Adding latitude of Los Angeles
coordinates.append(-118.2437)  # Adding longitude of Los Angeles
print("Updated coordinates:", coordinates)


points = [
    [35.6895, 139.6917],  # Tokyo
    [34.0522, -118.2437],  # Los Angeles
    [51.5074, -0.1278],  # London
    [48.8566, 2.3522],  # Paris
]

centroid_lat = sum([point[0] for point in points]) / len(points)
centroid_lon = sum([point[1] for point in points]) / len(points)
centroid = [centroid_lat, centroid_lon]
print("Centroid of the points is at: {:.2f} {:.2f}".format(centroid[0], centroid[1]))