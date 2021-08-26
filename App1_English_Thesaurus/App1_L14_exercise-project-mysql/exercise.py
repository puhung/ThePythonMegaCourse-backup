import mysql.connector

#establish a connection, after define this, execute this file. If there is no error, this means you are right
con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

#use this cursor object to navigate through the table of database
cursor = con.cursor()

# get input from the user
word = input("Enter a word: ")

# select all from the dictionary, which is the name of the table
# query = cursor.execute("SELECT * FROM Dictionary")
# return one tuple of a certain expression
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " %word)

#get the actual data
results = cursor.fetchall()

if results:
    for result in results: 
        print(result[1])
else:
    print('No word found')