import csv
import time
from twilio.rest import Client
from Utils.environmentVars import Environment_variables
from Utils.messageTemplate import MessageTemplate

env = Environment_variables()
msg_tem = MessageTemplate()

csv_file = 'contacts.csv'
msg_cost = 0.0079
TIMEOUT_SECONDS = 2
msg = msg_tem.returnMessage("Tikka Masala", "ReadyPickUp")



account_sid = env.get_Account_Sid()
auth_token = env.get_Auth_token()
from_number = env.get_number()

with open(csv_file, 'r') as csvfile:
    peoplereader = csv.reader(csvfile)
    numbers = set([p[0] for p in peoplereader])

messages = len(numbers)
cost = msg_cost * messages

print("> {} messages of 1 segments each will be sent, at a cost of ${} ".format(messages, cost))

client = Client(account_sid, auth_token)

for num in numbers:
    print("sending to " + num +"\n")
    message = client.messages \
                .create(
                    to = num,
                    from_=from_number,
                    body=msg
                )
    time.sleep(TIMEOUT_SECONDS)
    