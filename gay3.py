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



corpus='A mouse was having a very bad time. She could find no food at all. She looked here and there, but there was no food, and she grew very thin. At last the mouse found a basket, full of corn. There was a small hole in the basket, and she crept in. She could just get through the hole. Then she began to eat the corn. Being very hungry, she ate a great deal, and went on eating and eating. She had grown very fat before she felt that she had had enough. When the mouse tried to climb out of the basket, she could not. She was too fat to pass through the hole. " How shall I climb out?" said the mouse. "oh, how shall I climb out?" Just then a rat came along, and he heard the mouse. "Mouse," said the rat, "if you want to climb out of the basket, you must wait till you have grown as thin as you were when you went in."'
types=0
tokens=10
number=1
db.create_all()
new_person=User(number,corpus,types,tokens)
db.session.add(new_person)
    
    #Create corpus 2
corpus='A wolf carried off a lamb. The lamb said, " I know you are going to eat me, but before you eat me I would like to hear you play the flute. I have heard that you can play the flute better than anyone else, even the shepherd himself." The wolf was so pleased at this that he took out his flute and began to play. When he had done, the lamb insisted him to play once more and the wolf played again. The shepherd and the dogs heard the sound, and they came running up and fell on the wolf and the lamb was able to get back to the flock.'
types=1
tokens=11
number=2
db.create_all()
new_person=User(number,corpus,types,tokens)
db.session.add(new_person)
    
#Create corpus 3
corpus='A man had a little dog, and he was very fond of it. He would pat its head, and take it on his knee, and talk to it. Then he would give it little bits of food from his own plate. A donkey looked in at the window and saw the man and the dog. "Why does he not make a pet of me?" said the donkey. "It is not fair. I work hard, and the dog only wags its tail, and barks, and jumps on its masters knee. It is not fair." Then the donkey said to himself, "If I do what the dog does, he may make a pet of me." So the donkey ran into the room. It brayed as loudly as it could. It wagged its tail so hard that it knocked over a jar on the table. Then it tried to jump on to its masters knee. The master thought the donkey was mad, and he shouted, "Help! Help!" Men came running in with sticks, and they beat the donkey till it ran out of the house, and they drove it back to the field. "I only did what the dog does," said the donkey," and yet they make a pet of the dog, and they beat me with sticks. It is not fair."'
#masters
types=2
tokens=12
number=3
db.create_all()
new_person=User(number,corpus,types,tokens)
db.session.add(new_person)    
db.session.commit()

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
