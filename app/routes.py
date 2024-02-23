from app import app
from app.controller import EventEmailController, DataEmailController
from flask import request
from mailchecker import check_event_mail

@app.route('/')
def index():
    # check_event_mail()
    return 'Tes Mail Check'

@app.route('/save_emails', methods=['GET','POST'])
def save_emails():
    if request.method == 'GET':
        return EventEmailController.index()
    else:
        return EventEmailController.save()

@app.route('/recipient', methods=['GET','POST'])
def recipient():
    if request.method == 'GET':
        return DataEmailController.index()
    else:
        return DataEmailController.save()