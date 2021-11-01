import ReadSMS as r_sms
import SendSMS as s_sms

from flask import Flask,request

app = Flask(__name__)

@app.route("/get_message", methods=["GET"])
def get_message():
    script = r_sms.read_sms()
    return script


@app.route("/send_message", methods=["POST"])
def send_message():
    body_request = request.get_json()

    destination = body_request["destination"]
    message = body_request["message"]

    message = s_sms.send_sms(destination, message)
    return message

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')


