from flask import Flask, flash, render_template, Response, request, redirect, url_for,jsonify, session
from flask_sqlalchemy import SQLAlchemy
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import string
import random
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.dbExp'
dbExp = SQLAlchemy(app)
"""The database for the Experiment"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.dbQuiz'
dbQuiz = SQLAlchemy(app)
"""The database for the Quiz"""

class Experiment(dbExp.Model):
    """Class used to represent experiments in database. Various columns are created in the database."""
    id = dbExp.Column(dbExp.Integer, primary_key=True)
    corpus = dbExp.Column(dbExp.String(100), unique=True)
    types = dbExp.Column(dbExp.String(100), unique=False)
    tokens = dbExp.Column(dbExp.String(100), unique=False)
    numtypes=dbExp.Column(dbExp.Integer, unique=False)
    numtokens=dbExp.Column(dbExp.Integer, unique=False)

    def __init__(self, content, types, numtypes, tokens, numtokens):
        self.corpus = content
        self.types = types
        self.tokens = tokens
        self.numtypes= numtypes
        self.numtokens= numtokens

    def __repr__(self):
        return '<Experiment %r>' % self.corpus


@app.route("/")
def mainP():
    """This route renders the Introduction page"""
    return render_template('Introduction.html')

@app.route("/introduction")
def intro():
    """This route renders the Introduction page"""
    return render_template('Introduction.html')

@app.route("/feedback")
def feedbac():
    """This route renders the Feedback page"""
    return render_template('Feedback.html')

@app.route("/objective")
def obj():
    """This route renders the Objective page"""
    return render_template('Objective.html')

@app.route("/procedure")
def pro():
    """This route renders the Procedure page"""
    return render_template('Procedure.html')

@app.route("/theory")
def the():
    """This route renders the Theory page"""
    return render_template('Theory.html')

@app.route("/further-readings")
def fur():
    """This route renders the Further Readings page"""
    return render_template('Further Readings.html')

@app.route('/exp')
def indExp():
    """This route renders the Experiment page, also sends options for the select button"""
    return render_template('Experiment.html',data=[{'name':'Corpus1'}, {'name':'Corpus2'}, {'name':'Corpus3'}])

@app.route("/addexp" , methods=['GET', 'POST'])
def popexp():
    """This route is accessed by the admin to populate the experiment database"""
    try:
        corpus="A good wine is a wine that you like."
        tokens=word_tokenize(corpus.translate(str.maketrans('', '', string.punctuation)))
        tokens=[b.lower() for b in tokens]
        numtokens=len(tokens)
        types=[PorterStemmer().stem(b) for b in tokens]
        types=set(types)
        numtypes=len(types)
        tokens='-'.join(tokens)
        types='-'.join(types)
        dbExp.create_all()
        new_corpus=Experiment(corpus,types,numtypes, tokens, numtokens)
        dbExp.session.add(new_corpus)

        corpus="Just then a rat came along, and he heard the mouse."
        tokens=word_tokenize(corpus.translate(str.maketrans('', '', string.punctuation)))
        tokens=[b.lower() for b in tokens]
        numtokens=len(tokens)
        types=[PorterStemmer().stem(b) for b in tokens]
        types=set(types)
        numtypes=len(types)
        tokens='-'.join(tokens)
        types='-'.join(types)
        dbExp.create_all()
        new_corpus=Experiment(corpus,types,numtypes, tokens, numtokens)
        dbExp.session.add(new_corpus)

        corpus="I am eating what I am eating, even if I did eat it before."
        tokens=word_tokenize(corpus.translate(str.maketrans('', '', string.punctuation)))
        tokens=[b.lower() for b in tokens]
        numtokens=len(tokens)
        types=[PorterStemmer().stem(b) for b in tokens]
        types=set(types)
        numtypes=len(types)
        tokens='-'.join(tokens)
        types='-'.join(types)
        dbExp.create_all()
        new_corpus=Experiment(corpus,types,numtypes, tokens, numtokens)
        dbExp.session.add(new_corpus)

        dbExp.session.commit()
        return "added"
    except:
        """If the database has already been populated the unique parameter prevents it from repopulating and throws exception"""
        return "already added"


@app.route('/expr', methods=['GET', 'POST'])
def expr():
    """This route is called on pressing Go button to send the content of the experiment to the page"""

    data=[{'name':'Corpus1'}, {'name':'Corpus2'}, {'name':'Corpus3'}]
    global entry
    select = request.form.get('comp_select')
    if select == 'Corpus1':
        entry=Experiment.query.filter_by(id=1).first()
        send=entry.corpus
        return render_template('Experiment.html', content=send, data=data)
    if select == 'Corpus2':
        entry=Experiment.query.filter_by(id=2).first()
        send=entry.corpus
        return render_template('Experiment.html', content=send,  data=data)
    if select == 'Corpus3':
        entry=Experiment.query.filter_by(id=3).first()
        send=entry.corpus
        return render_template('Experiment.html', content=send,  data=data)



@app.route("/check" , methods=['GET', 'POST'])
def check():
    """On pressing the submit button this route reads the data from the form and
     checks if the answer is correct by seeing corresponding answer in the
     database. Entry is a global variable so it can access the value set in /expr.
      If not set it throws an exception. Input type also needs to be integer."""

    data=[{'name':'Corpus1'}, {'name':'Corpus2'}, {'name':'Corpus3'}]
    global entry

    try:
        send = entry.corpus
    except:
        send="Please select corpus and press Go"
        return render_template('Experiment.html', content=send, data=data)

    tokens=request.form.get('tokens')
    types= request.form.get('types')

    try:
        tokens=int(tokens)
        types=int(types)
        if tokens == entry.numtokens and types == entry.numtypes:
            results="Correct"
        else:
            results="Incorrect:"
        token_con = (entry.tokens).split('-')
        type_con = (entry.types).split('-')
        return render_template('Experiment.html', content=send, data=data, results=results, token_num=entry.numtokens, type_num=entry.numtypes, Tokens='Tokens', token=token_con, Types='Types', type=type_con)
    except:
        results="Enter Integer input"
        return render_template('Experiment.html', content=send, data=data, results=results)


class Quiz(dbQuiz.Model):
    """Class used to represent experiments in database. Various columns are created in the database."""
    id = dbQuiz.Column(dbQuiz.Integer, primary_key=True)
    question = dbQuiz.Column(dbQuiz.String(1000), unique=True)
    numtypes=dbQuiz.Column(dbQuiz.Integer, unique=False)
    numtokens=dbQuiz.Column(dbQuiz.Integer, unique=False)

    def __init__(self, content, numtypes, numtokens):
        self.question = content
        self.numtypes= numtypes
        self.numtokens= numtokens

    def __repr__(self):
        return '<Experiment %r>' % self.question

@app.route("/addquiz" , methods=['GET', 'POST'])
def popquiz():
    """This route is accessed by the admin to populate the quiz database"""
    try:
        question="What are you doing?"
        tokens=word_tokenize(question.translate(str.maketrans('', '', string.punctuation)))
        tokens=[b.lower() for b in tokens]
        numtokens=len(tokens)
        types=[PorterStemmer().stem(b) for b in tokens]
        types=set(types)
        numtypes=len(types)
        dbQuiz.create_all()
        new=Quiz(question,numtypes,numtokens)
        dbQuiz.session.add(new)

        question="Two and two makes four."
        tokens=word_tokenize(question.translate(str.maketrans('', '', string.punctuation)))
        tokens=[b.lower() for b in tokens]
        numtokens=len(tokens)
        types=[PorterStemmer().stem(b) for b in tokens]
        types=set(types)
        numtypes=len(types)
        dbQuiz.create_all()
        new=Quiz(question,numtypes,numtokens)
        dbQuiz.session.add(new)

        question="Ram eats an apple after eating a banana."
        tokens=word_tokenize(question.translate(str.maketrans('', '', string.punctuation)))
        tokens=[b.lower() for b in tokens]
        numtokens=len(tokens)
        types=[PorterStemmer().stem(b) for b in tokens]
        types=set(types)
        numtypes=len(types)
        dbQuiz.create_all()
        new=Quiz(question,numtypes,numtokens)
        dbQuiz.session.add(new)

        question="April will come here after 10th of April."
        tokens=word_tokenize(question.translate(str.maketrans('', '', string.punctuation)))
        tokens=[b.lower() for b in tokens]
        numtokens=len(tokens)
        types=[PorterStemmer().stem(b) for b in tokens]
        types=set(types)
        numtypes=len(types)
        dbQuiz.create_all()
        new=Quiz(question,numtypes,numtokens)
        dbQuiz.session.add(new)

        question="John drinks tea and George takes cold drink."
        tokens=word_tokenize(question.translate(str.maketrans('', '', string.punctuation)))
        tokens=[b.lower() for b in tokens]
        numtokens=len(tokens)
        types=[PorterStemmer().stem(b) for b in tokens]
        types=set(types)
        numtypes=len(types)
        dbQuiz.create_all()
        new=Quiz(question,numtypes,numtokens)
        dbQuiz.session.add(new)

        dbQuiz.session.commit()
        return "added"
    except:
        return "already added"


@app.route("/quiz", methods=['GET','POST'])
def dispq():
    """This route returns any three random questions from the database of quiz every
    time the quizzes page is opened. It sends the content to the Quizzes.html"""
    data=random.sample(range(1, 5), 3)
    itr=0
    global q
    global r
    q=[]
    r=[]
    for element in data:
        entry=Quiz.query.filter_by(id=element).first()
        q.append(entry.question)
        r.append(element)
    return render_template('Quizzes.html', ques1={'con':q[0]}, ques2={'con':q[1]}, ques3={'con':q[2]})


@app.route("/quiz-check", methods=['GET','POST'])
def checkq():
    """On pressing the submit button this route reads the data from the form and
     checks if the answer is correct by seeing corresponding answer in the
     database. r and q are global variables so it can access the value set in /quiz.
      If not set it throws an exception. Input type also needs to be integer."""
    score=0
    global r
    global q

    token1=request.form.get('tok1')
    type1=request.form.get('type1')
    token2=request.form.get('tok2')
    type2= request.form.get('type2')
    token3=request.form.get('tok3')
    type3= request.form.get('type3')

    try:
        entry1 = Quiz.query.filter_by(id=r[0]).first()
        entry2 = Quiz.query.filter_by(id=r[1]).first()
        entry3 = Quiz.query.filter_by(id=r[2]).first()
    except:
        return render_template('Quizzes.html', ques1={'con':" "},ques2={'con':" "}, ques3={'con':" "}, message= "Please reselect the 'Quizzes' option")

    try:
        if entry1.numtypes==int(type1) and entry1.numtokens==int(token1):
            score=score+1
        if entry2.numtypes==int(type2) and entry2.numtokens==int(token2):
            score=score+1
        if entry3.numtypes==int(type3) and entry3.numtokens==int(token3):
            score=score+1
        return render_template('Quizzes.html', score=score, ques1={'con':q[0], 'ans1':entry1.numtokens, 'ans2':entry1.numtypes}, ques2={'con':q[1], 'ans1':entry2.numtokens, 'ans2':entry2.numtypes}, ques3={'con':q[2], 'ans1':entry3.numtokens, 'ans2':entry3.numtypes})
    except:
        return render_template('Quizzes.html', ques1={'con':q[0]}, ques2={'con':q[1]}, ques3={'con':q[2]}, message="Enter integer inputs")


if __name__=='__main__':
    app.run(debug=True)
