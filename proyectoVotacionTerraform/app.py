import re
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

config = {
    'user': 'root',
    'password': 'root',
    'host': 'mysql',
    'db': 'voting_data',
}


def removePunctuationSymbols(text):
    """Elimina simbolos de puntuación de un texto dado."""
    accepted_chars = re.compile(r'[^0-9a-z]')
    text = accepted_chars.sub(' ', text).strip()
    return re.sub(' +', '', text)


@app.route('/', methods=['GET', 'POST'])
def votingCatsDogs():
    """Obtener datos para la página web."""
    try:
      if request.method == 'POST':
        # db = Database(config)
        # if request.form.get('cat') == 'votar':
        #  db.vote('votation','cat')
        # elif request.form.get('dog') == 'votar':
        #  db.vote('votation','dog')
        cats = 0
        dogs = 0
        # db.close()
        return render_template('voting.html', dog_votes= "Número de votos: " + str(dogs), cat_votes= "Número de votos: " + str(cats))
      return render_template('voting.html', dog_votes= "", cat_votes= "")

    except:
      message = {
          'message': 'Error internal'
      }
      resp = jsonify(message)
      resp.status_code = 500
      return resp
