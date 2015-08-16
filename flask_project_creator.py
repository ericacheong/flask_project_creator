
# flask_project_creator.py

from sys import argv
import os


# get application name from argv

if len(argv) > 1:
    script, app_name = argv
    if app_name == "-v":
        print "Usage: python flask_project_creator.py your_flask_application_name"
    else:
        # top folder and files
        first_dir_list = ['config','instance',app_name]
        gitignore_content = "instance\\\n*.pyc"
        runserver_content = "from %s import app\n\napp.run(host='0.0.0.0', port=5000)" % app_name
        start_content = "#!/bin/bash\n\nexport APP_CONFIG_FILE=%s/%s/config/development.py\n\npython runserver.py" % (os.getcwd(),app_name)
        first_file_list = ['.gitignore','runserver.py','start.sh']
        first_file_content = [gitignore_content,runserver_content,start_content]

        # config folder
        config_file_list = ['__init__.py','default.py','development.py','production.py']
        default_content = "# default.py\n\nDEBUG = False\nTESTING = False"
        development_content = "# development.py\n\nDEBUG = True"
        production_content = "# production.py\n\nDEBUG = False\nTESTING = False"
        config_file_content = ["", default_content, development_content, production_content]

        # instance folder
        config_content = "\nSECRET_KEY = 'SECRET KEY'"

        # app_name folder
        app_dir_list = ['static','templates']
        app_file_list = ['__init__.py','models.py','views.py']
        app_init_content = "from flask import Flask\n\napp = Flask(__name__, instance_relative_config=True)\n\n"
        app_init_content += "app.config.from_object('config.default')\n\napp.config.from_pyfile('config.py')\n\n"
        app_init_content += "app.config.from_envvar('APP_CONFIG_FILE')\n\nimport %s.views" % app_name
        app_view_content = "from %s import app\n\n@app.route('/')\ndef index():\n\treturn 'Hello World!'" % app_name
        app_file_content = [app_init_content, "", app_view_content]


        # templates folder
        temp_list = ["layout.html", "index.html", "login.html"]

        try:
            # create top root folder
            os.makedirs(app_name)
            os.chdir(app_name)

            # create top directories and files
            for d in first_dir_list:
                os.makedirs(d)
            for f, c in zip(first_file_list, first_file_content):
                fi = open(f, "wb")
                fi.write(c)
                fi.close()

            # config folder
            os.chdir('config')
            for f, c in zip(config_file_list, config_file_content):
                fi = open(f, "wb")
                fi.write(c)
                fi.close()

            # instance folder
            os.chdir('../instance')
            fi = open('config.py', 'wb')
            fi.write(config_content)
            fi.close()

            # app_name folder
            os.chdir("../%s" % app_name)
            for d in app_dir_list:
                os.makedirs(d)

            for f, c in zip(app_file_list, app_file_content):
                fi = open(f, "wb")
                fi.write(c)
                fi.close()

            os.chdir("static")
            fi = open("style.css", "wb")
            fi.close()

            os.chdir("../templates")
            for f in temp_list:
                fi = open(f, "wb")
                fi.close()

            # write runserver.py
            # fi = open("runserver.py", "wb")
            # content = "from %s import app\n\napp.debug = True\napp.run(host='0.0.0.0', port=5000)" % app_name
            # fi.write(content)
            # fi.close()

            # os.makedirs(app_name)
            # os.chdir(app_name)

            # # write __init__.py
            # fi = open("__init__.py", "wb")
            # content = "from flask import Flask\n\napp = Flask(__name__)\nimport %s.views" % app_name
            # fi.write(content)
            # fi.close()

            # # write views.py
            # fi = open("views.py", "wb")
            # content = "from %s import app\n\n@app.route('/')\ndef index():\n\treturn 'Hello World!'" % app_name
            # fi.write(content)
            # fi.close()

            # os.makedirs("static")
            # os.makedirs("templates")
            
        except:
            raise
else: 
    print "Please input one application name."

