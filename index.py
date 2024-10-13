from flask import Flask, Flask, request, jsonify, render_template
#poniendo un comentario
app = Flask(__name__)

@app.route('/')
def home():
     return render_template('home.html')
 
@app.route('/conceptos')
def conceptos():
     return render_template('conceptos.html')

@app.route('/teoria')
def teoria():
     return render_template('teoria.html')

@app.route('/juego1')
def juego1():
     return render_template('juego1.html')

@app.route('/juego2')
def juego2():
     return render_template('juego2.html')

@app.route('/juego3')
def juego3():
     return render_template('juego3.html')

@app.route('/api/receive-data', methods=['POST'])
def receive_data():
    data = request.json  # Recibir datos JSON desde el frontend
    # Aquí puedes procesar los datos como desees
    print(data)  # Puedes imprimirlos en la consola por ejemplo

    # Por ejemplo, devolver una respuesta JSON
    response = {'message': 'Datos recibidos correctamente'}
    return jsonify(response)
 
if __name__ == '__main__':
    app.run(debug=True)
    
    