import os
import sendgrid
from django.core import validators


def sendgrid_mail(to_email, subject, message):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

    data = {
        "personalizations": [
            {
                "to": [
                    {
                        "email": to_email
                    }
                ],
                "subject": subject
            }
        ],
        "from": {
            "email": 'battlezone@codebizz.tech',
            "name": "DTU BattleZone"
        },
        "content": [
            {
                "type": "text/html",
                "value": message
            }
        ]
    }
    response = sg.client.mail.send.post(request_body=data)


def verify_email(user):
    try:
        validators.validate_email(str(user.email).strip())
        return True
    except:
        print 'Invalid Email'
        return False
