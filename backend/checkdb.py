from app import db, BeginnerBird, AdvancedBird, app

with app.app_context():
    # Print all birds in the BeginnerBird table
    beginner_birds = BeginnerBird.query.all()
    print("Beginner Birds:")
    for bird in beginner_birds:
        print(f"ID: {bird.id}, Name: {bird.name}, Image: {bird.image}")

    # Print all birds in the AdvancedBird table
    advanced_birds = AdvancedBird.query.all()
    print("\nAdvanced Birds:")
    for bird in advanced_birds:
        print(f"ID: {bird.id}, Name: {bird.name}, Image: {bird.image}")