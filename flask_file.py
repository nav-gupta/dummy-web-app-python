import requests
from requests.auth import HTTPBasicAuth
from twilio.rest import TwilioRestClient
from flask import Flask, render_template, request
from configobj import ConfigObj

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def home(name=None):
    return render_template('home.html', name=name)

@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'GET':
        return render_template('message.html', name="bro")
    else:
        number = request.form['phoneNumber']
        message = request.form['message']
        client = TwilioRestClient(TWILIO_SID, TWILIO_TOKEN)
        message = client.message.create(body=message, to="+1" + number, from_=TWILIO_NUMBER) #replace with your TWILIO number.
    return render_template('message.html', success="fuck off.")
if __name__ == '__main__':
    app.run()
