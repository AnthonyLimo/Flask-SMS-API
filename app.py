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

#recieve and send the SMS on the AT API

@app.route("/sms-sending", methods=["GET","POST"])
def sms_sending(): 

    print(request.args.view_keys())

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

