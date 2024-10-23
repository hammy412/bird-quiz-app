from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure database URI for SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///birds.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Bird model
class Bird(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)

# Create the database and table
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    # Query all birds from the database
    bird = random.choice(Bird.query.all())
    session['current_bird'] = bird.id
    session['score'] = session.get('score', 0)
    return render_template('index.html', bird=bird)

@app.route('/guess', methods=['POST'])
def guess():
    guess = request.form.get('guess', '').strip().lower()
    bird_id = session['current_bird']
    bird = Bird.query.get(bird_id)
    
    if guess == bird.name.lower():
        session['score'] += 1
        result = "Correct!"
    else:
        result = f"Wrong! The correct answer was {bird.name}."
    
    # Load a new random bird
    new_bird = random.choice(Bird.query.all())
    session['current_bird'] = new_bird.id
    return render_template('index.html', bird=new_bird, result=result, score=session['score'])

if __name__ == '__main__':
    app.run(debug=True)