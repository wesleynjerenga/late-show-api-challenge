from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Guest(db.Model):
    __tablename__ = 'guests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    occupation = db.Column(db.String(120), nullable=False)
