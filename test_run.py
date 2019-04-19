from flask_testing import TestCase
from run import *
from flask import Flask 
import requests



def test_popquiz():
    """Testing if quiz class object is instantiated correctly"""
    newquiz=Quiz("question",1,1)
    assert newquiz.question=="question"
    assert newquiz.numtypes==1
    assert newquiz.numtokens==1


def test_popexp():
    """Testing if experiment class object is instantiated correctly"""
    newexp=Experiment("content","content",1,"content",1)
    assert newexp.corpus=="content"
    assert newexp.types=="content"
    assert newexp.numtypes==1
    assert newexp.tokens=="content"
    assert newexp.numtokens==1


def test_dbExp():
    """Making sure the database for experiment is populated and nltk is giving accurate answer"""
    x=Experiment.query.filter_by(id=1).first()
    assert x.numtokens==9
    assert x.numtypes==7

    x=Experiment.query.filter_by(id=2).first()
    assert x.numtokens==11
    assert x.numtypes==11

    x=Experiment.query.filter_by(id=3).first()
    assert x.numtokens==14
    assert x.numtypes==9

def test_dbQuiz():
    """Making sure the database for quiz is populated and nltk is giving accurate answer"""

    x=Quiz.query.filter_by(id=1).first()
    assert x.numtokens==4
    assert x.numtypes==4

    x=Quiz.query.filter_by(id=2).first()
    assert x.numtokens==5
    assert x.numtypes==4

    x=Quiz.query.filter_by(id=3).first()
    assert x.numtokens==8
    assert x.numtypes==7

    x=Quiz.query.filter_by(id=4).first()
    assert x.numtokens==8
    assert x.numtypes==7

    x=Quiz.query.filter_by(id=5).first()
    assert x.numtokens==8
    assert x.numtypes==7

class MyTest(TestCase):
    """ Testing that status code of all the urls is 200, ie successfully opened.
    """
    SERVER="http://127.0.0.1:5000/"
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 0
        return app

    def test_Main(self):
        r=requests.head("http://127.0.0.1:5000/")
        self.assertEqual(r.status_code,200)

        #r=requests.head("http://127.0.0.1:5000/expr")
        #self.assertEqual(r.status_code,200)
  
    def test_check(self):
        r=requests.head("http://127.0.0.1:5000/check")
        self.assertEqual(r.status_code,200)
   
    def test_quiz(self):
        r=requests.head("http://127.0.0.1:5000/quiz")
        self.assertEqual(r.status_code,200)
    
    def test_quiz_check(self):
        r=requests.head("http://127.0.0.1:5000/quiz-check")
        self.assertEqual(r.status_code,200)
    
    def test_exp(self):
        r=requests.head("http://127.0.0.1:5000/exp")
        self.assertEqual(r.status_code,200)
    
    def test_intro(self):
        r=requests.head("http://127.0.0.1:5000/introduction")
        self.assertEqual(r.status_code,200)

    def test_feedback(self):
        r=requests.head("http://127.0.0.1:5000/feedback")
        self.assertEqual(r.status_code,200)
    
    def test_objective(self):
        r=requests.head("http://127.0.0.1:5000/objective")
        self.assertEqual(r.status_code,200)
    
    def test_procedure(self):
        r=requests.head("http://127.0.0.1:5000/procedure")
        self.assertEqual(r.status_code,200)
    
    def test_theory(self):
        r=requests.head("http://127.0.0.1:5000/theory")
        self.assertEqual(r.status_code,200)
    
    def test_further_readings(self):
        r=requests.head("http://127.0.0.1:5000/further-readings")
        self.assertEqual(r.status_code,200)


    
