import mysql.connector

class Database:
    def __init__(self, name):
        self._conn = mysql.connector.connect(**name)
        self._cursor = self._conn.cursor(buffered=True)

    def getVotes(self,category):
        sql = "SELECT count(*) FROM votation WHERE category = '{}'".format(category)
        self._cursor.execute(sql)
        category_votes = self._cursor.fetchone()
        return category_votes[0]
    
    def vote(self,category):
        sql = "INSERT INTO votation(category) VALUES ('{}') ".format(category)
        self._cursor.execute(sql)
        self._conn.commit()

    def close(self):
        self._conn.close()
        self._cursor.close()

