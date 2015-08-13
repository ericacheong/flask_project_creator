
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
            os.makedirs(app_name)
            os.chdir(app_name)
            os.makedirs("static")
            os.makedirs("templates")
            fi = open("__init__.py", "wb")
            fi.close()
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

