from app import db
import json

class DataEmail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self):
        return '<DataEmail {}>'.format(self.email)