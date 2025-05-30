# Workbox
Workbox is a simple system to simplify the work for teachers and students alike.
> [!NOTE]  
> Make sure to fill in the necessary information.
## Quick Setup
1. Make a [PythonAnywhere](https://www.pythonanywhere.com/pricing/) account.
2. Confirm your email address.
3. Open the web tab, add a new web app, pick the "Flask" framework with "Python 3.13".
4. Enter the path "/home/YOUR_USERNAME/Workbox/src/api.py" to be added to the Flask project.
5. Create a new Bash console and enter these commands:
```
rm -rf /home/YOUR_USERNAME/Workbox/
git clone https://github.com/SeafoodStudios/Workbox
pip3 install -q -U google-genai
```
5. Go to your "Account" tab, select the "API Token" button and create a new API key.
6. Go to your web tab and reload the code.
7. Fill in the API key and the information required into this code and run it in a Zsh/Bash terminal.
```
curl -X POST https://YOUR_USERNAME.pythonanywhere.com/edit_settings/ \
-H "Content-Type: application/json" \
-d '{
  "password": "YOUR_API_KEY",
  "information": "# This is configuration for your server, edit this using the REST API.\nsetting_your_email = \"YOUR_EMAIL@EXAMPLE.COM\"\nsetting_your_password = \"YOUR_GOOGLE_APP_PASSWORD\"\nsetting_your_gemini_api_key = \"YOUR_GEMINI_API_KEY\"\nsetting_student_emails = [\"STUDENT_EMAIL@EXAMPLE.COM\"]\nsetting_parent_emails = [\"PARENT_EMAIL@EXAMPLE.COM\"]\nprojectname = \"WORKBOX\"\n'
}'
```
7. Go to your web tab and reload the code.
8. Go to your site, and it should be up!
