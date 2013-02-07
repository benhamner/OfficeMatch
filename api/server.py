import flask
from flask_sqlalchemy import SQLAlchemy
import datetime
import flask.ext.restless

app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Postgres1234@/officematch'
db = SQLAlchemy(app)

#def allow_origins(request):
#    request.headers.add('Access-Control-Allow-Origin', '*')
#    request.headers.add('Access-Control-Max-Age', '21600')
#    request.headers.add('Access-Control-Allow-Methods', '')
#
#app.process_response = allow_origins

# Don't currently have teams

class Organizations(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.VARCHAR)

class Sports(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.VARCHAR)
    bigger_score_better = db.Column(db.Boolean)
    date_created = db.Column(db.Date)

class Leagues(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.VARCHAR)
    organization_id = db.Column(db.BigInteger)
    sport_id = db.Column(db.BigInteger, db.ForeignKey("sports.id"))
    date_created = db.Column(db.Date)

class Users(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.VARCHAR)
    organization_id = db.Column(db.BigInteger, db.ForeignKey("sports.id"))
    date_created = db.Column(db.Date)

class Games(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    date_created = db.Column(db.Date)
    date_played = db.Column(db.Date)
    league_id = db.Column(db.BigInteger, db.ForeignKey("leagues.id"))

class Scores(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    game_id = db.Column(db.BigInteger)
    user_id = db.Column(db.BigInteger, db.ForeignKey("users.id"))
    score = db.Column(db.Float)

db.create_all()
manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Organizations, methods=['GET', 'POST'], results_per_page=1000)
manager.create_api(Sports, methods=['GET', 'POST'], results_per_page=1000)
manager.create_api(Leagues, methods=['GET', 'POST'], results_per_page=1000)
manager.create_api(Games, methods=['GET', 'POST'], results_per_page=1000)
manager.create_api(Scores, methods=['GET', 'POST'], results_per_page=1000)
app.run()