from flask import Flask, Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
     return render_template('home.html')
 
@app.route('/about')
def about():
     return render_template('about.html')




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