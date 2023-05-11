# *--> Importamos la libreria que vamos a usar en nuestro proyecto, en este caso Flask
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin


# *--> la libreria render_template para colocar una pagina principal.
# *--> la libreria request para obtener los datos que se van a enviar a partir de los diferentes formulacios html que se van a generar.
# *--> tambien se va a importa la libreria flask_cors que nos va a permitir de manera eficiente que nuestro servidor nuestra API responda en los diferentes puertos en inconvenientes del firewall.

# *--> Una vez importado esto tambien vamos a importar quienes son los que nos consultan las acciones, entonces vamos a importar nuestros controladores.

from controllers.userControllers import *

# *--> Se armara la estructura habitual para generar el proyecto con flask

# *--> generamos una variable app que va a ser instanciada en flask(__name__), con esta ya la instanciamos.

app = Flask(__name__)

# *--> el anterior procedimiento tambien lo vamos a hacer con cors

cors = CORS(app) # *--> practicamente va a estar indexado en nuestra app. practicamente se va a enrutar con las routes de nuestra app y va a estar atento a cualquier peticion que se haga por ese puerto.

# *-->  Generamos unas configuraciones de las cabeceras. [aqui colocamos el tipo de cabecera] y de una vez le decimos cualos son los tipos de cabecera.

app.config['CORS_HEADERS'] = 'Content-type' # *--> que contengan algun tipo de archivo.




# * --> ******************  CREACION DE RUTAS DE LA API ******************


# *--> Ruta para obtener los usuarios.
# *--> VER USUARIOS
# *--> en el caso personal le cree una ruta api y que contiene un modulo llamado users.

@app.route('/api/users')
@cross_origin() # *--> añadimos el @cross_origen donde le decimos que va a tener diferentes origenes.
def getAllUsers():
    return verUsuariosControllers()
# *--> definimos la funcion y le vamos a retornar el controlador verUsuariosController.

# *--> VER CONSULTA DE USUARIOS --> en este caso dependiendo de la palabra clave y seria el nombre de usuario basicamente la funcion buscar. A nivel de estructura va a ser la misma que el anterior.

@app.route('/api/users/<user>') # *--> añadimos el identificador <user> en este caso el nombre de usuario
@cross_origin() 
def getUsers(user): 
    return verUsuariosControllers(user)


# *-->  CREAR USUARIOS y ACTUALIZAR USUARIOS
# *-->  Para esta seccion, va a ser la misma funcion pero a diferencia de crear en actualizar usare el id del usuario a modificar o actualizar. 
# *--> usaremos el metodo POST 

@app.route('/api/users', methods=['POST'])
@cross_origin()

# *--> Esta funcion va a ejecutarme dos funciones distintas.

# *--> haremos unas condicionales, si tiene id modificar si no tiene id crear.
# *--> si tiene un id en la peticion en formato JSON request.json, crearemos basicamente una variable que se llama result que va a ejecutar una funcion que se va a llamar una funcion updateUser() y en caso contrario vamos a ejecutar una funcion que se va a llamar createUser(). y que nos retorne el resultado.

def createUpdateUsers():
    if 'id' in request.json:
        result = updateUser()
    else:
        result = createUser()
    return result

# *--> creamos las funciones que van dentro de createUpdateUsers()

def createUser(): # *--> va a obtener los datos y los va a convertir en formato lista.
    datos = [
        request.json['user'], # *--> importante en el formulario html en el atributo name coloquemos user.
        request.json['email'],
        request.json['password'] 
        ]
    return crearUsuariosController(datos) # *--> estos son los datos que vimos al crear los modelos y controladores que vienen del formulario del frontend.
    # *--> toma los datos que se van a mandar en formato JSON


def updateUser():
    datos = [
        request.json['id'], 
        request.json['user'], 
        request.json['email'],
        request.json['password'] 
        ]
    return modificarUsuariosController(datos)  

# *--> Resumen de la funcion createUpdateUsers()
# *--> El llega a la ruta si tiene un id, llama la funcion update, ésta toma los datos que se envian mediante JSON, mediante el metodo POST se las manda al controlador el controlador se las envia al modelo el modelo ejecuta la operacion, retorna los datos si lo pudo hacer o no y si lo pudo hacer basicamente nos mostraria el mensaje en formato JSON. 



# *-->  CREAR BORRAR USUARIOS

@app.route('/api/users/<id>', methods=['DELETE'])# *--> enviamos el id del usuario a borrar, seguido del metodo DELETE.
@cross_origin()

def removeUser(id):
    
    return borrarUsuariosController(id)


# *--> CREAMOS UNA RUTA RAIZ

@app.route('/')
@cross_origin()

def index():
    # return render_template('index.html')                         
    return('SERVIDOR ON')



# ********************************** FIN **********************************************
# ********************************** FIN **********************************************
# ********************************** FIN **********************************************


# *--> Esta linea va a al final, para que ejecute nuestro proyecto
# *--> ahora hacemos una condicional si el archivo que tenemos nombrado es igual al archivo principal si todo esto es correcto corremos nuestra aplicacion y podemos estructurar el puerto y el moden que estamos estructurando.  voy a trabajar en el puerto 3000 y en modo debug de desarrollo, para que el servidor automaticamente se actualice.  Con esto podemos empezar a generar las funciones.

if __name__ == '__main__':
    app.run(port = 3000, debug = True)