from flask import Flask, render_template, request, session, redirect, flash
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
class BeginnerBird(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)

class AdvancedBird(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)


# Create the database and table
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    mode = request.form.get('mode')
    num_questions = int(request.form.get('num_questions', 5))

    # Easy mode could be based on shorter names or some criteria you set
    if mode == 'beginner':
        birds = BeginnerBird.query.all() 
    else:
        birds = AdvancedBird.query.all()

    if not birds:
        flash("Failed to retrieve bird data from database.", "warning")
        return redirect('/')

    # Shuffle and limit the number of birds to the number of questions
    random.shuffle(birds)
    session['quiz_birds'] = [bird.id for bird in birds[:num_questions]]
    session['current_index'] = 0
    session['score'] = 0
    session['num_questions'] = num_questions
    session['mode'] = mode

    return redirect('/guess')

@app.route('/guess', methods=['GET', 'POST'])
def guess():
    if request.method == 'GET':
        if 'quiz_birds' not in session or session['current_index'] >= session['num_questions']:
            flash("Quiz over! Your final score is {}.".format(session.get('score', 0)), "info")
            return redirect('/')

        current_index = session['current_index']
        bird_id = session['quiz_birds'][current_index]

        if session['mode'] == 'beginner':
            bird = BeginnerBird.query.get(bird_id)
        else:
            bird = AdvancedBird.query.get(bird_id)    
        
        return render_template('guess.html', bird=bird, score=session['score'])

    elif request.method == 'POST':
        guess = request.form.get('guess', '').strip().lower()
        current_index = session['current_index']
        bird_id = session['quiz_birds'][current_index]

        if session['mode'] == 'beginner':
            bird = BeginnerBird.query.get(bird_id)
        else:
            bird = AdvancedBird.query.get(bird_id)  

        if bird and guess == bird.name.lower():
            session['score'] += 1
            result = "Correct!"
        else:
            result = f"Wrong! The correct answer was {bird.name}."

        session['current_index'] += 1

        if session['current_index'] >= session['num_questions']:
            flash("Quiz over! Your final score is {}.".format(session['score']), "info")
            return redirect('/')
        else:
            next_bird_id = session['quiz_birds'][session['current_index']]
            if session['mode'] == 'beginner':
                next_bird = BeginnerBird.query.get(next_bird_id)
            else:
                next_bird = AdvancedBird.query.get(next_bird_id)
    
            return render_template('guess.html', bird=next_bird, result=result, score=session['score'])

@app.route('/reset')
def reset():
    session.clear()
    flash("Quiz reset successfully.", "success")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)