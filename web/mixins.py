from django.conf import settings
from twilio.rest import Client
import random
class MessageHandler:
    phone_number = None
    otp = None

    def __init__(self,phone_number,otp) -> None:
        self.phone_number = phone_number
        self.otp = otp

    def send_otp_on_phone(self):
        client = Client(settings.TWILIO_SID, settings.TWILIO_AUTH_TOKEN)

        message = client.messages.create(
                                    body=f'your otp is {self.otp}',
                                    from_='+12184007822',
                                    to= self.phone_number
                                )

        print(message.sid)

