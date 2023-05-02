import re
from flask import Flask, render_template, request, Response, jsonify
from back import Database

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
          db = Database(config)
          if request.form.get('cat') == 'votar':
             db.vote('votation', 'cat')
          elif request.form.get('dog') == 'votar':
              db.vote('votation', 'dog')
          cats = db.getVotes('votation', 'cat')
          dogs = db.getVotes('votation', 'dog')
          db.close()
          return render_template('voting.html', dog_votes="Número de votos: " + str(dogs), cat_votes="Número de votos: " + str(cats))
        return render_template('voting.html', dog_votes="", cat_votes="")
    except:
        message = {
            'message': 'Error internal'
        }
        resp = jsonify(message)
        resp.status_code = 500
        return resp


@app.route('/api/v1/vote/<votation>', methods=['POST'])
def vote(votation):
  """Votar en una categoría."""
  try:
    if request.is_json:
      data = request.get_json()
      votation = removePunctuationSymbols(votation)
      category = removePunctuationSymbols(data['category'])
      db = Database(config)

      if not db.checkVotingExists(votation):
        db.close()
        message = {
            'message': 'Voting does not exist'
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
      if not db.checkCategoryExists(votation, category):
        db.close()
        message = {
            'message': 'Category does not exist'
        }
        resp = jsonify(message)
        resp.status_code = 400
        return resp

      db.vote(votation, category)
      db.close()
      return Response(status=200)
    return Response(status=403)
  except:
    message = {
        'message': 'Error internal'
    }
    resp = jsonify(message)
    resp.status_code = 500
    return resp


@app.route('/api/v1/new', methods = ['POST'])
def newVotation():
  """Crear una nueva votación."""
  if request.is_json:
      data = request.get_json()
      votation = removePunctuationSymbols(data['name'])
      db = Database(config)

      if db.checkVotingExists(votation):
        db.close()
        message = {
            'message': 'Voting exist'
        }
        resp = jsonify(message)
        resp.status_code = 400
        return resp

      categories = list(data['categories'].values())
      categories = [removePunctuationSymbols(c) for c in categories]
      db.createVoting(votation, categories)
      return Response(status=200)
  return Response(status=403)


@app.route('/api/v1/reset/<votation>', methods = ['DELETE'])
def reset(votation):
  """Resetear una votación."""
  try:
    votation = removePunctuationSymbols(votation)
    db = Database(config)

    if not db.checkVotingExists(votation):
      db.close()
      message = {
          'message': 'Voting does not exist'
      }
      resp = jsonify(message)
      resp.status_code = 404
      return resp

    db.resetVoting(votation)
    return Response(status=200)
  except:
    message = {
        'message': 'Error internal'
    }
    resp = jsonify(message)
    resp.status_code = 500
    return resp


@app.route('/api/v1/drop/<votation>', methods = ['DELETE'])
def drop(votation):
  """Eliminar una votación."""
  try:
    votation = removePunctuationSymbols(votation)
    db = Database(config)

    if not db.checkVotingExists(votation):
      db.close()
      message = {
          'message': 'Voting does not exist'
      }
      resp = jsonify(message)
      resp.status_code = 404
      return resp

    db.deleteVoting(votation)
    return Response(status=200)
  except:
    message = {
        'message': 'Error internal'
    }
    resp = jsonify(message)
    resp.status_code = 500
    return resp


@app.route('/api/v1/<votation>/<category>', methods=['GET'])
def getCategoryVotes(votation, category):
  """Obtener votos de una categoría en una votación."""
  try:
    votation = removePunctuationSymbols(votation)
    category = removePunctuationSymbols(category)
    db = Database(config)

    if not db.checkVotingExists(votation):
      db.close()
      message = {
          'message': 'Voting does not exist'
      }
      resp = jsonify(message)
      resp.status_code = 404
      return resp
    if not db.checkCategoryExists(votation, category):
      db.close()
      message = {
          'message': 'Category does not exist'
      }
      resp = jsonify(message)
      resp.status_code = 404
      return resp

    votes = db.getVotes(votation, category)
    db.close()
    message = {
        'category': category,
        'value': votes
    }
    resp = jsonify(message)
    resp.status_code = 200
    return resp

  except:
    message = {
        'message': 'Error internal'
    }
    resp = jsonify(message)
    resp.status_code = 500
    return resp
