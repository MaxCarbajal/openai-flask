from flask import Flask, render_template
app = Flask(__name__)

## rutas

# principal
@app.route('/')
def raiz():
    return render_template('inicio.html')

# ruta nosotros
@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

# bloque de prueba
if __name__ == '__name__':
    app.run(debug=True)