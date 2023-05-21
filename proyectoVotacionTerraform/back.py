import mysql.connector


class Database:
    """Clase para conectar con la BBDD y ejecutar las consultas."""

    def __init__(self, name):
        """Constructor de la clase."""
        self._conn = mysql.connector.connect(**name)
        self._cursor = self._conn.cursor(buffered=True)

    def initDatabase(self):
        sql = """
                CREATE TABLE votation (
                    id int not null AUTO_INCREMENT,
                    category ENUM('cat', 'dog') NOT NULL,
                    PRIMARY KEY (id)
                )
            """
        self._cursor.execute(sql)
        self._conn.commit()
        sql = """
                INSERT INTO votation(category) VALUES ('cat'), ('dog'), ('cat'), ('dog'), ('dog')
            """
        self._cursor.execute(sql)
        self._conn.commit()
 
    def getVotes(self, table, category):
        """Obtener el número de votos de una categoría."""
        sql = "SELECT count(*) FROM {} WHERE category = '{}'".format(table, category)
        self._cursor.execute(sql)
        category_votes = self._cursor.fetchone()
        return category_votes[0]

    def vote(self, table, category):
        """Insertar un nuevo voto en una votación."""
        sql = "INSERT INTO {}(category) VALUES ('{}') ".format(table, category)
        self._cursor.execute(sql)
        self._conn.commit()

    def checkVotingExists(self, table):
        """Comprobar si existe la votación."""
        sql = "SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '{}'".format(table)
        self._cursor.execute(sql)
        if self._cursor.fetchone()[0] == 1:
            return True
        return False

    def checkCategoryExists(self, table, category):
        """Comprobar si existe la categoría."""
        sql = """
                select trim(leading 'enum' from col.column_type) as enum_values
                from information_schema.columns col
                where col.data_type in ('enum') and col.table_name = '{}'
            """.format(table)
        self._cursor.execute(sql)
        return category in self._cursor.fetchone()[0]

    def createVoting(self, table, categories):
        """Crear nueva tablade votación."""
        stringCategories = ','.join("'%s'" % (c) for c in categories)
        sql = """
                CREATE TABLE {} (
                    id int not null AUTO_INCREMENT,
                    category ENUM({}) NOT NULL,
                    PRIMARY KEY (id)
                )
        """.format(table, stringCategories)
        self._cursor.execute(sql)
        self._conn.commit()

    def deleteVoting(self, table):
        """Eliminar una tabla de votación."""
        sql = "DROP TABLE {}".format(table)
        self._cursor.execute(sql)
        self._conn.commit()

    def resetVoting(self, table):
        """Eliminar todos los registros de una tabla de votación."""
        sql = "TRUNCATE TABLE {}".format(table)
        self._cursor.execute(sql)
        self._conn.commit()

    def close(self):
        """Cerrar la conexión con la BBDD."""
        self._conn.close()
        self._cursor.close()
