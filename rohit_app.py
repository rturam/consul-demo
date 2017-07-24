from flask import Flask
import mysql.connector
import requests
#from urllib2 import urlopen
import urllib
import json
from mysql.connector import errorcode

app = Flask(__name__)

answer = urllib.urlopen("http://192.168.65.1:8500/v1/catalog/service/mysql").read()
#data = json.loads(response.read())
print (answer)

try:
    decoded = json.loads(answer)
    dbip = decoded[0]['ServiceAddress']
    dbport = decoded[0]['ServicePort']
except (ValueError, KeyError, TypeError):
    print "JSON format error"

try:
    import MySQLdb


    db = MySQLdb.connect(host="mysql",user="root",passwd="root",db="mysql")       # name of the data base

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    # Use all the SQL you like
    cur.execute("SELECT * FROM db")

    # print all the first cell of all the rows
    for row in cur.fetchall():
        print row[0]

    db.close()


    print("**********in side for conn")
    cnx = mysql.connector.connect(host="mysql",user="root",passwd="root",db="mysql")

    if cnx.is_connected():
            print('Success! Connected to MySQL database')

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

cursor = cnx.cursor()

try:
   message = cursor.execute("""SELECT message_str FROM messages WHERE message_no=1""")
except:
   cnx.rollback()

cursor.close()
cnx.close()



@app.route('/')
def hello():
    return 'Hi, \n'.format(message)
if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=False)
