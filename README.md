
## About APP

Hello, This is And App using python flask with sqlaclhemy mysql

## Endpoints

- **GET /**: Home endpoint to test the application.
  
- **POST /save_emails**: Save email details along with the timestamp for sending.

  - Request:
    ```json
    {
        "event_id": 1,
        "email_subject": "Email Subject",
        "email_content": "Email Body",
        "timestamp": "15 Dec 2015 23:12"
    }
    ```

  - Response (Success):
    ```json
    {
        "message": "Email saved successfully"
    }
    ```

- **GET /recipient**: Get all recipients or save a new recipient.

- **POST /recipient**: Save a new recipient.

  - Request:
    ```json
    {
        "email": "recipient@example.com"
    }
    ```

  - Response (Success):
    ```json
    {
        "message": "Recipient saved successfully"
    }
    ```


**You need to setup database first in file .env**

## Thank You
