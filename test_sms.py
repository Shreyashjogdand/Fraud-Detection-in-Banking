from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, USER_PHONE_NUMBER

try:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="Test SMS from my bank project",
        from_=TWILIO_PHONE_NUMBER,
        to=USER_PHONE_NUMBER
    )
    print("SUCCESS! Message SID:", message.sid)
except Exception as e:
    print("FAILED:", e)