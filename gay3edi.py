#!/usr/bin/env python
# from flask import Flask, flash, redirect, render_template, \
#      request, url_for
#
# app = Flask(__name__)
from flask import Flask, flash, render_template, Response, request, redirect, url_for
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#db.drop_all()
#db.session.commit()
#Base.metadata.drop_all(db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True)
    corpus = db.Column(db.String(1000), unique=False)
    types = db.Column(db.Integer, unique=False)
    tokens = db.Column(db.Integer, unique=False)

    def __init__(self, number, username, email,roll):
        self.corpus = username
        self.types = email
        self.tokens = roll
        self.number=number

    def __repr__(self):
        return '<User %r>' % self.corpus


@app.route('/')
def index():
    return render_template('Experiment.html',data=[{'name':'Corpus1'}, {'name':'Corpus2'}, {'name':'Corpus3'}])


#entry = User.query.filter_by(number=1).first()
@app.route("/test" , methods=['GET', 'POST'])
def test():
    data=[{'name':'Corpus1'}, {'name':'Corpus2'}, {'name':'Corpus3'}]
    global entry
    select = request.form.get('comp_select')
    if select == 'Corpus1':
        entry=User.query.filter_by(number=1).first()
        send=entry.corpus
        return render_template('Experiment.html', content=send, data=data)
    if select == 'Corpus2':
        entry=User.query.filter_by(number=2).first()
        send=entry.corpus
        return render_template('Experiment.html', content=send,  data=data)
    if select == 'Corpus3':
        entry=User.query.filter_by(number=3).first()
        send=entry.corpus
        return render_template('Experiment.html', content=send,  data=data)

@app.route("/check" , methods=['GET', 'POST'])
def check():
    data=[{'name':'Corpus1'}, {'name':'Corpus2'}, {'name':'Corpus3'}]
    #throws an exception if not integers
    tokens=int(request.form['tokens'])
    types= int(request.form['types'])
    select =request.form.get('comp_select')
    send=entry.corpus
    if tokens == entry.tokens and types == entry.types:
        results="Correct"
    else:
        results="Incorrect"
    return render_template('Experiment.html', content=send, data=data, results=results, tokens=entry.tokens, types=entry.types)

if __name__=='__main__':
    app.run(debug=True)
