from . import db

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    air_date = db.Column(db.Date, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'air_date': self.air_date.isoformat() if self.air_date else None
        }
