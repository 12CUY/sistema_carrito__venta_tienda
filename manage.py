# sera el script que utilizamos para gestionar la aplicacion(flask-script)

from flask_script import Manager
from aplicacion.app import app
# creacion de la interfaz || debug habilita el depurador de flask
manager = Manager (app)
app.config['DEBUG'] = True

# inicia la aplicacion  de flask
if  __name__ == '__main__': 
    manager.run()