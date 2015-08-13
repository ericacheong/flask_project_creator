
# flask_project_creator.py

from sys import argv
import os

# get application name from argv

if len(argv) > 1:
    script, app_name = argv
    if app_name == "-v":
        print "Usage: python flask_project_creator.py your_flask_application_name"
    else:
        try:
            os.makedirs(app_name)
            os.chdir(app_name)
            # write runserver.py
            fi = open("runserver.py", "wb")
            content = "from %s import app\n\napp.debug = True\napp.run(host='0.0.0.0', port=5000)" % app_name
            fi.write(content)
            fi.close()

            os.makedirs(app_name)
            os.chdir(app_name)

            # write __init__.py
            fi = open("__init__.py", "wb")
            content = "from flask import Flask\n\napp = Flask(__name__)\nimport %s.views" % app_name
            fi.write(content)
            fi.close()

            # write views.py
            fi = open("views.py", "wb")
            content = "from %s import app\n\n@app.route('/')\ndef index():\n\treturn 'Hello World!'" % app_name
            fi.write(content)
            fi.close()

            os.makedirs("static")
            os.makedirs("templates")
            
            os.chdir("static")
            fi = open("style.css", "wb")
            fi.close()
            os.chdir("../templates")
            fi_list = ["layout.html", "index.html", "login.html"]
            for f in fi_list:
                fi = open(f, "wb")
                fi.close()
        except:
            raise
else: 
    print "Please input one application name."

