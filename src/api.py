import smtplib
from email.message import EmailMessage
from flask import Flask, request, jsonify
import settings
from google import genai
import requests

app = Flask(__name__)

@app.route('/submit/', methods=['POST'])
def submit():
    data = request.get_json()
    sender = data.get('sender')
    receiver = settings.setting_your_email
    password = data.get('password')
    subject = data.get('subject')
    body = data.get('body')
    if sender in settings.setting_student_emails:
        if all([sender, receiver, password, subject, body]):
            client = genai.Client(api_key=str(settings.setting_your_gemini_api_key))
            response = client.models.generate_content(
                model="gemini-2.0-flash", contents="Give a short grade summary (with a letter grade, and if you think it is made by AI, say that) for this Python homework (do NOT add comments): " + str(body)
            )
            grade = str(response.text)
            msg = EmailMessage()
            msg['Subject'] = "Workbox Submission: " + subject
            msg['From'] = sender
            msg.set_content(str(body) + "\nHere is a grade summary: \n" + str(grade))
            html_content = f"""
            <html>
              <body>
                <h2>Here is the completed Python Homework:</h2>
                <p>{body}</p>
                <h2>Here is a grade summary: </h2>
                <p>{grade}</p>
              </body>
            </html>
            """
            msg.add_alternative(html_content, subtype='html')
            try:
                with smtplib.SMTP('smtp.gmail.com', 587) as server:
                    server.starttls()
                    server.login(sender, password)

                    msg['To'] = receiver
                    server.send_message(msg)

                    del msg['To']

                    msg['To'] = settings.setting_parent_emails[settings.setting_student_emails.index(sender)]
                    server.send_message(msg)

            except Exception as e:
                return jsonify({"error": str(e)}), 500

            return jsonify({"message": "Submission sent successfully"}), 200
        else:
            return jsonify({"error": "Missing required fields"}), 400
    else:
        return jsonify({"error": "Email is not in students list."}), 400

@app.route('/edit_settings/', methods=['POST'])
def edit_settings():
    data = request.get_json()
    password = data.get('password')
    information = data.get('information')

    username = str(settings.projectname)

    response = requests.get(
        'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
            username=username
        ),
        headers={'Authorization': 'Token {token}'.format(token=password)}
    )

    if response.status_code == 200:
        file = open("settings.py", "w")
        file.write(str(information))
        file.close()
        return jsonify({"success": "Changed settings."}), 200
    else:
        return jsonify({"error": "Invalid password."}), 400
@app.route('/read_settings/', methods=['POST'])
def read_settings():
    data = request.get_json()
    password = data.get('password')

    username = str(settings.projectname)

    response = requests.get(
        'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
            username=username
        ),
        headers={'Authorization': 'Token {token}'.format(token=password)}
    )

    if response.status_code == 200:
        file = open("settings.py", "r")
        contents = str(file.read())
        file.close()
        return jsonify({"success": "Contents: \n" + contents}), 200
    else:
        return jsonify({"error": "Invalid password."}), 400
@app.route('/assign_work/', methods=['POST'])
def assign_work():
    data = request.get_json()
    receiver = data.get('receiver')
    password = data.get('password')
    message = data.get('message')
    subject = data.get('subject')
    body = data.get('body')
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(settings.setting_your_email, settings.setting_your_password)
            msg = EmailMessage()
            msg['Subject'] = "Workbox Homework: " + subject
            msg['From'] = settings.setting_your_email
            msg['To'] = receiver
            msg.set_content(body)
            server.send_message(msg)

            del msg['To']

            msg['To'] = settings.setting_parent_emails[settings.setting_student_emails.index(receiver)]
            server.send_message(msg)
            return jsonify({"success": "Assignment sent successfully!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
