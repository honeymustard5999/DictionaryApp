
# need to install mysql from terminal: pip3 install mysql-connector-python
# then import mysql
# next need a variable to store the connect()
# then need to add entries into connect(), one parameter each line with 'string' and ,
# Host IP is the IP of the server that has the database
# database is the parameter of the connect function


import mysql.connector
con = mysql.connector.connect(
user = 'ardit700_student',
password = 'ardit700_student',
host = '108.167.140.122',
database = 'ardit700_pm1database'
)

# now need to query the database
cursor = con.cursor()


word = input('Please enter a word: ')

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
# query = cursor.execute(" SELECT * FROM Dictionary WHERE Expression = 'line' ")
results = cursor.fetchall()   # fetch all the data and store in results, the result is a list[] made of tuples()

if results:
    for result in results:
        print(result[1])   # [1] means only definition
else:
    print('No results found.')