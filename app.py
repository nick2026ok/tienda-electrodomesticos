from flask import Flask                ##Del paquete flask, trae la herramienta flask para crear la aplicación web. Flask es un microframework de Python que facilita la creación de aplicaciones web.
app = Flask(__name__)                  ##Se definio una variable llamada "app" que contendra la aplicacion completa de Flask. El argumento __name__ se utiliza para indicar el nombre del módulo actual, lo que ayuda a Flask a localizar recursos y archivos relacionados con la aplicación.
productos = [
    {
        "id": 1,
        "nombre": "Heladera samsung",
        "precio": 25000,
    },
    {
        "id": 2,
        "nombre": "Microondas LG",
        "precio": 12000,
    },
    {
        "id": 3,
        "nombre": "Smart TV 50 pulgadas",
        "precio": 30000,
    }
]
@app.route("/")  ##cuando alguien visite esta direccion, ejecuta la funcion que viene debajo 
def inicio():    ##se esta creando una funcion llamada "inicio" que se ejecutará cuando se acceda a la ruta raíz ("/") de la aplicación. Esta función devuelve un mensaje simple indicando que el backend de ElectroShop está funcionando.
    return "Backend de ElectroShop funcionando"   ##Cuando se accede a la ruta raíz ("/") de la aplicación, esta función devuelve el mensaje "Backend de ElectroShop funcionando". Esto sirve como una verificación rápida para asegurarse de que el servidor está en funcionamiento y respondiendo a las solicitudes.
@app.route("/productos")  
def obtener_productos():
    return productos
if __name__ == "__main__": ##Si este archivo es el principal, ejecuta lo siguiente código. Esto es útil para asegurarse de que el servidor solo se inicie cuando se ejecute este archivo directamente, y no cuando se importe como un módulo en otro lugar.
    app.run(debug=True)  ##Esta linea enciende el servidor , sin ella flask existe pero no arranca. El argumento debug=True activa el modo de depuración, lo que proporciona información detallada sobre los errores y reinicia automáticamente el servidor cada vez que se realizan cambios en el código. Esto es especialmente útil durante el desarrollo, ya que facilita la identificación y corrección de errores.
  
  ##.\venv\Scripts\python.exe app.py es para ejecutar el servidor de Flask en modo de desarrollo. Esto iniciará la aplicación y permitirá que se acceda a ella a través de http://localhost:5000/. El servidor se reiniciará automáticamente cada vez que se realicen cambios en el código, lo que facilita el proceso de desarrollo.    