from twilio.rest import Client


account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)


message = client.messages.create(
    from_='whatsapp:+',  # Twilio Sandbox WhatsApp number
    body='',
    to='whatsapp:+'  # Your WhatsApp number
)
