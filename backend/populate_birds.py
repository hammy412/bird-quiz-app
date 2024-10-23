from app import db, BeginnerBird, AdvancedBird, app

beginner_birds_data = [
    {"name": "Northern Cardinal", "image": "cardinal.jpg"},
    {"name": "Blue Jay", "image": "bluejay.jpg"},
    {"name": "American Robin", "image": "robin.jpg"},
    {"name": "American Crow", "image": "crow.jpg"},
    {"name": "European Starling", "image": "starling.jpg"},
    {"name": "Northern Mockingbird", "image": "mockingbird.jpg"},
    {"name": "House Wren", "image": "housewren.jpg"},
    {"name": "House Finch", "image": "housefinch.jpg"},
    {"name": "American Goldfinch", "image": "goldfinch.jpg"},
    {"name": "Red-bellied Woodpecker", "image": "redbelly.jpg"},
    {"name": "Bald Eagle", "image": "america.jpg"},
    {"name": "Red-tailed Hawk", "image": "redtailed.jpg"},
    {"name": "Mallard", "image": "mallard.jpg"},
    {"name": "Mute Swan", "image": "swan.jpg"},
    {"name": "Tufted Titmouse", "image": "titmouse.jpg"}
]

advanced_birds_data = [
    {"name": "Peregrine Falcon", "image": "peregrine_falcon.jpg"},
    {"name": "Golden Eagle", "image": "golden_eagle.jpg"},
    {"name": "Barred Owl", "image": "barred-owl.jpg"},
    {"name": "Indigo Bunting", "image": "indigo-bunting.jpg"},
    {"name": "Great Blue Heron", "image": "great-blue-heron.jpg"},
    {"name": "Red-headed Woodpecker", "image": "red-headed-woodpecker.jpg"},
    {"name": "Belted Kingfisher", "image": "belted-kingfisher.jpg"},
    {"name": "Merlin", "image": "merlin.jpg"},
    {"name": "Snow Goose", "image": "snow-goose.jpg"},
    {"name": "Wood Thrush", "image": "wood-thrush.jpg"},
    {"name": "White-tailed Kite", "image": "white-tailed-kite.jpg"},
    {"name": "Baltimore Oriole", "image": "oriole.jpg"},
    {"name": "Ring-necked Duck", "image": "ring-necked-duck.jpg"},
    {"name": "Pine Grosbeak", "image": "pine-grosbeak.jpg"},
    {"name": "Glossy Ibis", "image": "glossy-ibis.jpg"}
]

with app.app_context():
    for bird_data in beginner_birds_data:
        bird_exists = BeginnerBird.query.filter_by(name=bird_data['name'], image=bird_data['image']).first()
        if not bird_exists:
            bird = BeginnerBird(name=bird_data['name'], image=bird_data['image'])
            db.session.add(bird)

    for bird_data in advanced_birds_data:
        bird_exists = AdvancedBird.query.filter_by(name=bird_data['name'], image=bird_data['image']).first()
        if not bird_exists:
            bird = AdvancedBird(name=bird_data['name'], image=bird_data['image'])
            db.session.add(bird)

    db.session.commit()  