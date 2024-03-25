import mysql.connector

# Create a connection to the MySQL server
connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='Satyam@01',
    database='moviesdb'
)

# Create a cursor object
cursor = connection.cursor()

# Execute a SQL query
cursor.execute('SELECT * FROM movies WHERE imdb_rating BETWEEN 6 AND 8;')

# Fetch the results of the query
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the cursor and connection objects
cursor.close()
connection.close()
