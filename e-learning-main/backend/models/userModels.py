# *--> generaremos las consultas necesarias para trabajar en nuestro proyecto

# *--> importamos de la carpeta db el dataSource y de ahi importamos la clase MysqlConect.

from db.dataSource import MysqlConect

# *--> importamos de la carpeta db el settings y de ahi importamos el diccionario conexionBD
# *--> donde tenemos la conexion hacia nuestra base de datos de MySql
from db.settings import conexionBD


# *--> generamos una variable en este caso es la instanciacion de dataSource
# *--> esta variable va a contener todos los datos para generar la conexion.

con = MysqlConect(
    conexionBD["host"],
    conexionBD["user"],
    conexionBD["password"],
    conexionBD["db"]

)

# *--> una vez teniendo todo en la variable vamos a generar las consultas, recordar que son solo consultas que me van a traer datos.

#*********************************** MODELO VER USUARIO ***************************************************************

# *--> la primer consulta es la de ver usuario.
# *--> creamos una funcion
# *--> En esta funcion vamos a añadir el id como vacio ya que mas adelante usaremos el metodo de buscar.

def verUsuariosModel(user=""):
    sql = """
        SELECT
            id,
            user,
            email,
            password     
        FROM
            users
                
    """
    # *--> En caso de que necesite ver un usuario en específico, necesitamos una condicion que nos permita alterar la tabla.

    # *--> Si al contar los datos del user estos no son igual a cero (0).  el programa me va a alterar la consulta de sql, al sql anterior. en esta me le va a agregar una consulta tipo WHERE donde.
    if len(user) != 0:
        sql += """            
            WHERE user like '%{0}%'
        
        """.format(user)
        
    # *--> una vez teniendo esto hacemos el retorno de los datos.
    return con.getData(sql) # *--> usamos la variable con seguido de getData incorporando la consulta sql.
                            # *--> el getData es el metodo que se creo en la clase MysqlConect.

    # *--> En resumen donde esta el WHERE user like '%{0}%' esta parte ultima donde esta los porcentajes, significa que se escribira una letra y dependiendo de la letra se filtrara en la columna de user.


# ******************************** MODELO CREAR USUARIO **************************************************************

# *--> Vamos a crear otro modelo que nos va a permitir crear usuarios.

def crearUsuariosModel(datos): # *--> importante tener los datos, y se da por sentado que vienen en formato de lista.                           En el controlador cuando lo creemos enviaremos los datos bien parametrizados.
    sql = '''
        INSERT INTO users
            (id, user, email, password)
        VALUES
            (NULL, '{0}', '{1}' , '{2}') # *--> si colocamos en INSERT el id, y como es autoincremental en VALUES colocamos, NULL, seguido de eso colocamos las posiciones, importante como los demas datos son varchard, colocarlos entre comillas simples.
    
    '''.format(datos[0], datos[1], datos[2]) # *--> en format le indicamos la posicion de los datos. datos[0] va a corresponder al usuario que estara en la posicion 0 y datos[1] corresponde al email que estara en la posicion 1 y datos[2] corresponde al password.
    
    # *--> teniendo esto necesitamos que el modelo lo ejecute y nos traiga la respuesta.
    return con.query(sql) # *--> El query lo traemos de la clase MysqlConect de dataSource.  El metodo query nos devuelve un booleano, nos retornara un True o un False.



# ******************************** MODELO MODIFICAR USUARIO ***********************************************************

def modificarUsuariosModel(datos):
    sql = '''

        UPDATE users
        SET
            user = '{1}',
            email = '{2}',
            password = '{3}'
        WHERE
            users.id = {0}
    
    
    '''.format(datos[0], datos[1], datos[2], datos[3]) # *--> vamos a traer la informacion donde datos[0] traemos el id, datos[1] traemos el usuario, datos[2] traemos el email, datos[3] traemos el password.

    # *--> una vez teniendo esto realizamos el return.

    return con.query(sql)



# ******************************** MODELO BORRAR USUARIO ***********************************************************

def borrarUsuariosModel(id):
    sql = '''

        DELETE FROM users
        WHERE 
            user.id = {0}
    
    '''.format(id)

    return con.query(sql)