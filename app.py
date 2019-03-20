from flask import Flask, request
from flask_cors import CORS
from flask_api import status

import africastalking

app = Flask(__name__)
CORS(app)

username = "sandbox"
api_key = "3eac8065cda866a26786969b3c610c0796d923c7d2ca10fe2a85008087e90782"

africastalking.initialize(username, api_key)

sms = africastalking.SMS

#Validation methods

def validate_phone_number(number):
    if isinstance(number, str):
        first_value = number[0]
        if first_value is "0":
            number.replace("0", "+254", 1)
        elif "+254" in  number:
            return number
        else:
            raise ValueError("This is not a valid phone number") 


def validate_message(message):
    if isinstance(message, str):
        return message
    else:
        raise ValueError("Not string based content") 

#recieve and send the SMS on the AT API

@app.route("/sms-sending", methods=["GET","POST"])
def sms_sending(): 
    
    data = request.get_json(force=True))
    message = data['message']
    phone_number = data['phoneNumber'] 

    try:
        sending_message = validate_message(message)
        sending_phone_number = validate_phone_number(phone_number)
    except Exception as e:
        return str(status.HTTP_400_BAD_REQUEST)

    try:
        response = sms.send(sending_message, sending_phone_number)
        print(response)
        return str(status.HTTP_200_OK)
    except Exception as e:
        print(f"Houston we have a problem {e}")
        return str(status.HTTP_500_INTERNAL_SERVER_ERROR )



#notify user on dashboard whether the SMS was sent or not

@app.route("/sending-notification", methods=["GET","POST"])
def sms_notification():
    pass


if __name__ == "__main__":
    app.run(debug=True)    

