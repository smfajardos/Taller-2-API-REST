from models.perro import Perro
from models.boaConstructor import BoaConstructor
from models.huron import Huron
from models.gato import Gato
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

def obtener_sonido(animal):
    if animal == 'Gato':
        return Gato.hacer_sonido(animal)
    elif animal == 'Perro':
        return Perro.hacer_sonido(animal)
    elif animal == 'Hurón':
        return Huron.hacer_sonido(animal)
    elif animal == 'Boa constrictor':
        return BoaConstructor.hacer_sonido(animal)
    else:
        return "Animal no encontrado"

@app.route('/sonido-animal', methods=['GET'])
def sonido_animal():
    animal = request.args.get('animal', '').capitalize()
    sound = obtener_sonido(animal)
    return jsonify({"animal": animal, "sound": sound})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)