from app import db, Bird, app

birds_data = [
    {"name": "Cardinal", "image": "cardinal.jpg"},
    {"name": "Blue Jay", "image": "bluejay.jpg"},
    {"name": "Robin", "image": "robin.jpg"}
]

with app.app_context():
    for bird_data in birds_data:
        bird = Bird(name=bird_data['name'], image=bird_data['image'])
        db.session.add(bird)

    db.session.commit()