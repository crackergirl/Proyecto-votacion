import time
from flask import Flask
import mysql.connector



app = Flask(__name__)


connection = mysql.connector.connect(
  user='root', password='root', host='mysql', port="3306", database='patata')
print("DB connected")

cursor = connection.cursor()
cursor.execute('Select * FROM users')
students = cursor.fetchall()
connection.close()

#print(students)

@app.route('/')
def hello():
    count = 1
    return 'Hello World! I have patata been seen {}.{} patata\n'.format(count,students)