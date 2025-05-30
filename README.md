1. Make a [PythonAnywhere](https://www.pythonanywhere.com/pricing/) account.
2. Open the web tab, add a new web app, pick the "Flask" framework with "Python 3.13".
3. Enter the path "/home/workboxtest/Workbox/src/api.py" to be added to the Flask project.
4. Create a new Bash console and enter these commands:
```
rm -rf /home/workboxtest/Workbox/
git clone https://github.com/SeafoodStudios/Workbox
pip3 install -q -U google-genai
```
5. Open the web tab and reload your app.
