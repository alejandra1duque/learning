import pymysql.cursors

class MysqlConect():
    
    # * Atributos
    # * creamos la variable que nos va a conectar a Mysql
    con = ''

    # * constructor
    # * creamos un metodo contructor para conectarnos a Myqsl
    def __init__(self, host, user, password, db) :
        
        # nos conectamos a la base de datos (metodo contructor )
        
        self.con =  pymysql.connect(
                    host = host,
                    user = user,
                    password = password,
                    db = db,
                    cursorclass = pymysql.cursors.DictCursor
                )
    # optener datos de la base de datos (select) 
    def getData(self, sql):
        cursor = self.con.cursor() # Se crea la variable cursor para almacenar los datos de la conexion a la base de datos que se configuro.
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    # ejecutar consultas (insert, delete, update)
    def query(self, sql):
        cursor = self.con.cursor()
        cursor.execute(sql)
        return self.con.commit()


