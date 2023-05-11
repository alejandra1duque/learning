# *-->  Vamos a importar todos los modelos primero que todo

from models.userModels import *  # *--> con el * importamos todos los modelos.

# *--> adicional usaremos una libreria de flask que se llama jsonify para convertir directamente a formato JSON cada uno de los parámetros para que posteriormente en las funciones o métodos tecnicamente este todo en formato JSON y que solamente el main.py tenga que ejecutarlo sin ningun problema y se pueda visualizar de manera correcta.

from flask import jsonify

# ********** CONTROLADOR VER USUARIOS *********************

def verUsuariosControllers(id=""): 
    # *--> igual que en los modelos agregamos un id en caso de que queramos filtrar  por un usuario en específico.
    datos = verUsuariosModel(id)
    # *--> una ves esto vamos a obtener los datos.  como los vamos a obtener?  Los vamos a obtener de la consulta que se nos ejecuta del modelo. Aca llamamos el modelo y le enviamos el id, si no enviamos el id el nos va a realizar una consulta de SELECT normal y si lo enviamos nos trae el id especifico.  Una vez obtenidos los datos debemos generar la estructura tipo JSON.

    result = []  # *--> creamos una variable que tendra el formato de lista por el momento pero mas adelante vamos a modificarlo en formato JSON.
    
    # *--> ESTRUCTURA FORMATO JSON
    # *--> al realizar la consulta verUsuariosModel(id) nos trae una lista, debemos recorrer fila por fila, creamos el ciclo for.
    for row in datos:
        contenido = {
            'id' : row['id'], # *--> trae el dato que es el id
            'user' : row['user'], # *--> trae el dato que es el usuario
            'email' : row['email'], # *--> trae el dato que es el email
            'password' : row['password'] # *--> trae el dato que es el password
        }
        # *--> como son muchos datos las vamos a agregar a la lista anteriormente creada en result.
        result.append(contenido) # *--> En result estaran todos los datos que traiga la consulta.
   
    # *--> una vez terminado salimos del ciclo for ya que sabemos que nos va a agregar mucha informacion a la variable result y estara todos nuestros datos. Pero necesitamos convertirlo a formato JSON usamos el jsonify para eso.
    return jsonify(result)
    # *--> En resumen se trajo los datos en que vienen en formato de lista los agregamos en otra lista y los convertimos o se les genero una estructura tipo JSON


# ********** CONTROLADOR CREAR USUARIOS *********************

def crearUsuariosController(datos):
# *--> Para crear usuarios necesitamos datos, y estos los vamos a capturar del archivo raiz del main.py para esta función vamos a dar por sentado que ya tenemos los datos. Esta funcion es muy sencilla solo necesitamos enviar los datos al modelo y que este nos retorne si fue True o fue False. y esta respuesta debemos capturarlo en formato JSON para hacer la respectiva validación.
    result = [ str( crearUsuariosModel(datos) ) ]
    # *--> tecnicamente nos devuelve un booleano, para que esto nos quede mejor estructurado lo metemos en formato de lista. Al momento de ejecutar el jsonify nos lo ejecute. Pero tenemos que convertirlo en string. por lo general envian un 0 o un 1.
    # *--> una vez tenemos la estructura del booleano necesitamos que la funcion nos retorne ese valor en formato JSON.
    return jsonify(result)


# ********** CONTROLADOR MODIFICAR Y BORRAR USUARIOS *********************

# *--> la estructura en esta parte es practicamente la misma

# ************************** CONTROLADOR MODIFICAR USUARIOS ******************

def modificarUsuariosController(datos):
    result = [ str( modificarUsuariosModel(datos) ) ]
    return jsonify(result)

# ************************** CONTROLADOR BORRAR USUARIOS ******************

def borrarUsuariosController(id):
    result = [ str( borrarUsuariosModel(id) ) ]
    return jsonify(result)
