import os
from twilio.rest import Client
import smtplib

# Using a .env file to retrieve the phone numbers and tokens.

class NotificationManager:

    def __init__(self):
        self.client = Client(os.environ['TWILLIO_SID'], os.environ["TWILLIO_AUTH"])
        self._smtpusername = os.environ['SMTP_USERNAME']
        self._smtppassword = os.environ['SMTP_PASSWORD']
        self._virtual = os.environ["TWILIO_VIRTUAL_NUMBER"]
        self._verified = os.environ["TWILIO_VERIFIED_NUMBER"]
        self.connection = smtplib.SMTP(os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"])
        self.smtp_address = os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"]

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=self._virtual,
            body=message_body,
            to=self._verified
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(self._smtpusername, self._smtppassword)
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self._smtpusername,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )
        

