"""
This program verifies that every animal in the animal database
eats at least one food.
"""

import mysql.connector
from database import login_info
#Create out cursor
db = mysql.connector.Connect(**login_info)
cursor = db.cursor()
# Get our animal data using SQL statement
cursor.execute('SELECT id FROM animal')
# Get all rows from the statement
animal_data = cursor.fetchall()
# Get our food data using SQL statement
cursor.execute('SELECT anid FROM food')
# Get all rows from the statement
food_data = cursor.fetchall()
# Compare our two data sets
if not set(animal_data) <= set(food_data):
    print('At least one animal is starving.')
else:
    print('All the animals are fed.')
# Close our db connection
cursor.close()