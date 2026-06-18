from flask import Flask
app = Flask(__name__)
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
@app.route("/")
def inicio():
    return "Backend de ElectroShop funcionando"
@app.route("/productos")
def obtener_productos():
    return productos
if __name__ == "__main__":
    app.run(debug=True)
  
  ##.\venv\Scripts\python.exe app.py es para ejecutar el servidor de Flask en modo de desarrollo. Esto iniciará la aplicación y permitirá que se acceda a ella a través de http://localhost:5000/. El servidor se reiniciará automáticamente cada vez que se realicen cambios en el código, lo que facilita el proceso de desarrollo.    