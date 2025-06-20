from .app import app
from .models import db, User, Guest, Episode, Appearance
from datetime import date

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create users
    user1 = User(username='admin')
    user1.set_password('password')
    db.session.add(user1)

    # Create guests
    guest1 = Guest(name='John Doe', occupation='Comedian')
    guest2 = Guest(name='Jane Smith', occupation='Actor')
    db.session.add_all([guest1, guest2])

    # Create episodes
    episode1 = Episode(date=date(2024, 6, 1), number=1)
    episode2 = Episode(date=date(2024, 6, 2), number=2)
    db.session.add_all([episode1, episode2])

    # Create appearances
    appearance1 = Appearance(rating=5, guest_id=1, episode_id=1)
    appearance2 = Appearance(rating=4, guest_id=2, episode_id=1)
    appearance3 = Appearance(rating=3, guest_id=1, episode_id=2)
    db.session.add_all([appearance1, appearance2, appearance3])

    db.session.commit()
    print('Database seeded!')
