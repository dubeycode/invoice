from flask import Flask, render_template, request, jsonify
import smtplib
from twilio.rest import Client

app = Flask(__name__)

# API for sending SMS (example with Twilio)
def send_sms(student_name, student_mobile, fee_amount):
    # Your Twilio account SID and Auth Token
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"Dear {student_name}, you have successfully paid ₹{fee_amount} for your fee.",
        from_='+19477297781',  # Your Twilio phone number
        to=student_mobile
    )
    return message.sid

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_sms', methods=['POST'])
def send_sms_api():
    data = request.get_json()
    student_name = data['student_name']
    student_mobile = data['student_mobile']
    fee_amount = data['fee_amount']

    # Send SMS using Twilio (or any other service)
    sms_status = send_sms(student_name, student_mobile, fee_amount)
    return jsonify({'status': 'SMS sent', 'sid': sms_status})

if __name__ == '__main__':
    app.run(debug=True)
