import mysql.connector

class Database:
    def __init__(self, name):
        self._conn = mysql.connector.connect(**name)
        self._cursor = self._conn.cursor(buffered=True)

    def getVotes(self,table,category):
        sql = "SELECT count(*) FROM {} WHERE category = '{}'".format(table,category)
        self._cursor.execute(sql)
        category_votes = self._cursor.fetchone()
        return category_votes[0]
    
    def vote(self,table,category):
        sql = "INSERT INTO {}(category) VALUES ('{}') ".format(table,category)
        self._cursor.execute(sql)
        self._conn.commit()

    def checkVotingExists(self,table):
        sql = "SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '{}'".format(table)
        self._cursor.execute(sql)
        if self._cursor.fetchone()[0] == 1:
            return True
        return False
    
    def checkCategoryExists(self,table, category):
        sql = """ 
                select trim(leading 'enum' from col.column_type) as enum_values
                from information_schema.columns col
                where col.data_type in ('enum') and col.table_name = '{}'
            """.format(table)
        self._cursor.execute(sql)
        return category in self._cursor.fetchone()[0]

    
    def createVoting(self,table,categories):
        stringCategories = ','.join("'%s'" % (c) for c in categories)
        sql = """ 
                CREATE TABLE {} (
                    id int not null AUTO_INCREMENT,
                    category ENUM({}) NOT NULL,
                    PRIMARY KEY (id)
                )
        """.format(table,stringCategories)
        self._cursor.execute(sql)
        self._conn.commit()
    
    def deleteVoting(self,table):
        sql = "DROP TABLE {}".format(table)
        self._cursor.execute(sql)
        self._conn.commit()

    def resetVoting(self,table):
        sql = "TRUNCATE TABLE {}".format(table)
        self._cursor.execute(sql)
        self._conn.commit()

    def close(self):
        self._conn.close()
        self._cursor.close()
