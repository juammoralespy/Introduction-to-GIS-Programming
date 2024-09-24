##Exercise 5: Parsing and Extracting Address Information
##Given a string in the format "Street, City, Country" (e.g., "123 Main St, Springfield, USA"),
##write a function that parses the string into a dictionary with keys street, city, and country.
##
##The function should return a dictionary like {"street": "123 Main St", "city": "Springfield", "country": "USA"}.


geographic_site = '123 Main St, Springfield, USA'

def geo_str_to_dict(string_geo):
    geo_dict = {}

    string_lst = string_geo.split(',')

    geo_dict['street'] = string_lst[0]
    geo_dict['city'] = string_lst[1]
    geo_dict['country'] = string_lst[2]

    return geo_dict

print(geo_str_to_dict(geographic_site))

    
