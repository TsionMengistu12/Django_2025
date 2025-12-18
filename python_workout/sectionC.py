########## question number 7

import json

json_data = """
{
"product" : "laptop",
"price" : 75000,
"available" : true
}
"""
data = json.loads(json_data)
print(data["product"])
print(data["price"])

product = data.get("product")
price = data.get("price")
print(product, price)

######### question number 8

user = {"username": "Tsion",
        "email": "tsionmeng@gmail.com",
        "active_status": True}

json_user = json.dumps(user)
print(json_user)

## save the JSON into file
with open("user.json", "w") as f:
    json.dump(user, f)

########## question number 9
from abc import ABC, abstractmethod
import json

json_data = """
[
{"type": "email"},
{"type": "sms"}
]
"""

class Notification(ABC):

    @abstractmethod
    def send(self):
        pass


class EmailNotification(Notification):
    def send(self):
        print("sending EMAIL notification")

class SMSNotification(Notification):
    def send(self):
        print("sending SMS notification")

notifications = json.loads(json_data)


for item in notifications:
    if item["type"] == "email":
        o = EmailNotification()
        o.send()

    elif item["type"] == "sms":
        o = SMSNotification()
        o.send()

######## question number 10

class Account(ABC):

    @abstractmethod
    def get_account_type(self):
        pass

class SavingsAccount(Account):
    def get_account_type(self):
        return "savings account"
    
class CurrentAccount(Account):
    def get_account_type(self):
        return "Current account"
    
import json

json_data = """
{
"type": "savings",
"type": "current"
}"""
account_data = json.loads(json_data)


        
