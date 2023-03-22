from flask import Flask, render_template, request,Response,jsonify
from back import Database

app = Flask(__name__)

config = {
    'user': 'root',
    'password': 'root',
    'host': 'mysql',
    'db': 'voting_data',
}

@app.route('/', methods=['GET','POST'])
def voting():
    try:
      if request.method == 'POST':
        db = Database(config)
        if request.form.get('cat') == 'votar':
          db.vote('cat')
        elif request.form.get('dog') == 'votar':
          db.vote('dog')
        cats = db.getVotes('cat')
        dogs = db.getVotes('dog')
        db.close()
        return render_template('voting.html', dog_votes= "Número de votos: " + str(dogs), cat_votes= "Número de votos: " + str(cats))
      return render_template('voting.html', dog_votes= "", cat_votes= "")
    
    except:
      message = {
        'message': 'Error internal'
      }
      resp = jsonify(message)
      resp.status_code = 500
      return resp

@app.route('/api/v1/votation/cats', methods=['GET'])
def getCats():
  try:
    db = Database(config)
    cats = db.getVotes('cat')
    db.close()
    message = {
       'cat_votes': cats
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
  
@app.route('/api/v1/votation/dogs', methods=['GET'])
def getDogs():
  try:
    db = Database(config)
    dogs = db.getVotes('dog')
    db.close()
    message = {
       'dog_votes': dogs
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
    
@app.route('/api/v1/votation/vote', methods = ['POST'])
def vote():
  try:
    if request.is_json:
      data = request.get_json()
      db = Database(config)
      db.vote(data['category'])
      db.close()
      return (Response(status=200))
    else:
      return (Response(status=403))
    
  except:
    message = {
       'message': 'Error internal'
    }
    resp = jsonify(message)
    resp.status_code = 500
    return resp
