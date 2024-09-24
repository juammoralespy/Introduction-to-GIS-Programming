##Exercise 4: String Normalization and Cleaning
##Given a list of city names with inconsistent formatting (e.g., [" new york ", "Los ANGELES", "   CHICAGO"]), normalize the names by:
##
##Stripping any leading or trailing whitespace.
##
##Converting them to title case (e.g., "New York", "Los Angeles", "Chicago").
##
##Ensure that the output is a clean list of city names.

cities = [" new york ","Los ANGELES","    CHICAGO"]

print('\nOrigin List: ',cities)

for x in range(len(cities)):
    cities[x] = cities[x].title().strip()

print('\nResult List: ',cities)
