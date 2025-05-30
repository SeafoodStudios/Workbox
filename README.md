1. Make a [PythonAnywhere](https://www.pythonanywhere.com/pricing/) account.
2. Open the web tab, add a new web app, pick the "Flask" framework with "Python 3.13".
3. Enter the path "/home/workboxtest/Workbox/src/api.py" to be added to the Flask project.
4. Create a new Bash console and enter these commands:
```
rm -rf /home/workboxtest/Workbox/
git clone https://github.com/SeafoodStudios/Workbox
pip3 install -q -U google-genai
```
5. Go to your "Account" tab, select the "API Token" button and create a new API key.
6. Fill in the API key and the information required into this code and run it in a Zsh/Bash terminal.
curl -X POST https://**YOUR_USERNAME**.pythonanywhere.com/edit_settings/ \
```
curl -X POST https://YOUR_USERNAME.pythonanywhere.com/edit_settings/ \
-H "Content-Type: application/json" \
-d '{
  "password": "YOUR_API_KEY",
  "information": "# This is configuration for your server, edit this using the REST API.\nsetting_your_email = \"your_email@example.com\"\nsetting_your_password = \"your_google_app_password\"\nsetting_your_gemini_api_key = \"your_gemini_api_key\"\nsetting_student_emails = [\"student_email@example.com\"]\nsetting_parent_emails = [\"parent_email@example.com\"]\nprojectname = \"workbox\"\n'
}'
```
