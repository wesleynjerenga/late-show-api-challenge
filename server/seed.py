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
    db.session.commit()

    # Create episodes
    episode1 = Episode(title='Premiere Night', air_date=date(2024, 6, 1))
    episode2 = Episode(title='Comedy Special', air_date=date(2024, 6, 2))
    db.session.add_all([episode1, episode2])
    db.session.commit()

    # Create appearances
    appearance1 = Appearance(rating=5, guest_id=guest1.id, episode_id=episode1.id)
    appearance2 = Appearance(rating=4, guest_id=guest2.id, episode_id=episode1.id)
    appearance3 = Appearance(rating=3, guest_id=guest1.id, episode_id=episode2.id)
    db.session.add_all([appearance1, appearance2, appearance3])

    db.session.commit()
    print('Database seeded!')
