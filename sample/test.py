import os, sys, time, json

from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message, MediaMessage

print "Environment", os.environ
try:
   os.environ["SELENIUM"]
except KeyError:
   print "Please set the environment variable SELENIUM to Selenium URL"
   sys.exit(1)

driver = WhatsAPIDriver(client='remote', command_executor=os.environ["SELENIUM"])
print("Waiting for QR")
driver.wait_for_login()

print("Bot started")

while True:
    time.sleep(3)
    print('Checking for more messages')
    for contact in driver.get_unread():
        for message in contact.messages:
            if isinstance(message, Message):  # Currently works for text messages only.
                contact.chat.send_message(message.content)
