from flask import Flask, request, jsonify
from flasgger import Swagger
import random

app = Flask(__name__)
swagger = Swagger(app)

jokes = ["Où se cachent les canards ? Dans le coin coin coin.",
         "Que dit un canard qui s'est perdu? Coin !",
         "Pourquoi un canard est toujours à l'heure ? Parce qu'il est dans l'étang."]

@app.route('/joke', methods=['GET', 'POST'])
def joke():
    """
    Renvoie une blague aléatoire en GET.
    Ajoute une nouvelle blague en POST.
    ---
    parameters:
      - name: joke
        in: body
        required: true
        schema:
          type: object
          properties:
            joke:
              type: string
              example: 'coin coin'
    responses:
      200:
        description: Une blague
      201:
        description: Blague enregistrée avec succès
      400:
        description: Erreur dans le format de la requête
    """
    if request.method == 'GET':
        joke = {"joke": random.choice(jokes)}
        return jsonify(joke)
    
    if request.method == 'POST':
        if not request.is_json:
            return 'Bad Request', 400
        
        data = request.get_json(silent=True)
        joke = data.get('joke')

        if len(joke) < 10:
            return jsonify({"error": "joke too short"})
        
        jokes.append(joke)
        return 'Created', 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)