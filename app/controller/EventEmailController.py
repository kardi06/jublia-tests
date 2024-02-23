from app.model.eventmail import EventMail
from app import response, app, db
from datetime import datetime
from flask import request

def index():
    try:
        m = EventMail.query.all()
        val = formatarray(m)
        return response.success(val,"success")
    except Exception as e:
        print(e)

def formatarray(datas):
    array = []

    for i in datas:
        array.append(singleObject(i))

    return array

def singleObject(data):
    data = {
        'event_id': data.event_id,
        'email_subject': data.email_subject,
        'email_content': data.email_content,
        'timestamp': data.timestamp
    }

    return data

def save():
    try:
        email_subject = request.form.get('email_subject')
        email_content = request.form.get('email_content')
        timestamp = request.form.get('timestamp')

        # Convert timestamp string to datetime object
        timestamp = datetime.strptime(timestamp, '%d %b %Y %H:%M')

        input = [{
            'email_subject': email_subject,
            'email_content': email_content,
            'timestamp': timestamp,
        }]

        emails = EventMail(email_subject=email_subject,email_content=email_content,timestamp=timestamp)
        db.session.add(emails)
        db.session.commit()

        return response.success(input, 'Success save emails')
    except Exception as e:
        print(e)
