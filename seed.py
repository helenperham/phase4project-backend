from app import app
from models import db, User, Photo

print('Seeding database ... 🌱')

with app.app_context():
    user1 = User('Helen Perham', 'helen@example.com', '12345')
    user2 = User('Shivani Jetty', 'shivani@example.com', '12345')
    db.session.add_all(
        [user1,user2])
    db.session.commit()

with app.app_context():
    photo1 = Photo('Sunset at the beach', '1')
    photo2 = Photo('Self Portrait', '1')
    db.session.add_all(
        [photo1, photo2])
    db.session.commit()

print('Done! 🌳')
