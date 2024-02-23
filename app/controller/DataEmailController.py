from app.model.dataemail import DataEmail
from app import response, app, db

from flask import request

def index():
    try:
        m = DataEmail.query.all()
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
        'id': data.id,
        'email': data.email,
    }

    return data

def save():
    try:
        email = request.form.get('email')

        input = [{
            'email': email,
        }]

        emails = DataEmail(email=email)
        db.session.add(emails)
        db.session.commit()

        return response.success(input, 'Success save emails')
    except Exception as e:
        print(e)