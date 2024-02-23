from app import db
from datetime import datetime

class EventMail(db.Model):
    event_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email_subject = db.Column(db.Unicode(100), nullable=False)
    email_content = db.Column(db.Unicode(200), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<EventMail {}>'.format(self.event_id)