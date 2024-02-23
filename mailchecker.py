import schedule
import time
from datetime import datetime, timedelta
from app import app
from app.model.dataemail import DataEmail
from app.model.eventmail import EventMail

def check_event_mail():
    try:
        # Get the current timestamp
        current_time = datetime.now()

        # Get EventMail entries where timestamp is less than or equal to current time and on the same day
        event_mails = EventMail.query.filter(EventMail.timestamp <= current_time,
                                              EventMail.timestamp >= current_time.replace(hour=0, minute=0, second=0)).all()

        for event_mail in event_mails:
            # Check if DataEmail is not empty
            if DataEmail.query.count() > 0:
                data_mail = DataEmail.query.all()
                for mail in data_mail:
                    # Print email_subject and email_content from EventMail
                    print(f"Send mail to: {mail.email}")
                    print(f"Email Subject: {event_mail.email_subject}")
                    print(f"Email Content: {event_mail.email_content}")

        # Wait for one minute before checking again
        # time.sleep(60)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Schedule the send_emails function to run every minute
    schedule.every(1).minutes.do(check_event_mail)

    # Run the Flask application
    app.run()