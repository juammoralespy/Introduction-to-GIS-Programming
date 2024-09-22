##Exercise 3: Building Dynamic SQL Queries
##Given a table name and a condition, dynamically build an SQL query string.
##
##Example: If table_name = "cities" and condition = "population > 1000000", the query should be "SELECT * FROM cities WHERE population > 1000000;".
##
##Add additional conditions dynamically, like AND clauses.

table = "cities"
condition = "population > 1000000"

query = '"SELECT * FROM ' + table + ' WHERE ' + condition + ';"'

print(query)

