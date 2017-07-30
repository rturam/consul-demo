from flask import Flask
import mysql.connector
import requests
import urllib
import json
import time
from mysql.connector import errorcode

from dns import resolver

app = Flask(__name__)

time.sleep(15)

print("**********in side DNSSSSSSSSSSSS")
consul_resolver = resolver.Resolver()
consul_resolver.port = 53
consul_resolver.nameservers = ["172.17.0.1"]

answer = consul_resolver.query("mysql.service.consul", 'A')
for answer_ip in answer:
    print(answer_ip)

    db_host=answer_ip
    print(db_host)
    
    grt_msg = ""
    try:
        print("**********in side for conn")
        cnx = mysql.connector.connect(host='{0}'.format(db_host),user="root",passwd="root",db="messages")
        if cnx.is_connected():
            print(' >>>>>>>>>>>>>>>>>>>>>>  Success! Connected to MySQL database')

            cursor = cnx.cursor(buffered=True)
            message = cursor.execute("""SELECT msg FROM greetings WHERE msg_no=1""")
            grt_msg = cursor.fetchone()[0]
            print(grt_msg)
            cursor.close()
            cnx.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
            cnx.rollback()
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            cnx.rollback()
        else:
            print(err)
            cnx.rollback()

@app.route('/')
def hello():
    html ='{0}'.format(grt_msg)
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080, debug=True)
