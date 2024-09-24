##Exercise 3: Building Dynamic SQL Queries
##Given a table name and a condition, dynamically build an SQL query string.
##
##Example: If table_name = "cities" and condition = "population > 1000000", the query should be "SELECT * FROM cities WHERE population > 1000000;".
##
##Add additional conditions dynamically, like AND clauses.

table = "cities"
condition = "population > 1000000"

query = '"SELECT * FROM ' + table + ' WHERE ' + condition + ';"'

print('\nCurrent expression:\n',query)

condition2 = "population < 5000000"

clause_And = False

option_dinamic = int(input('\nDo you like add the second condition (population < 5000000)? 1=yes, 0=no: ')) 


if option_dinamic == 1:
    query = '"SELECT * FROM ' + table + ' WHERE ' + condition + ' AND ' + condition2 + ';"'
    print('\n Final Expression: \n\n', query)
elif option_dinamic == 0:
    query = '"SELECT * FROM ' + table + ' WHERE ' + condition + ';"'
    print('\n Final Expression: \n\n', query)
else:
    print()
    print('x' * 50)
    print('{:^50}'.format('Option invalid... try again...'))
    print('x' * 50)

