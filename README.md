# Flask Project Creator

This script creates flask project template with the following folder layout as recommended in https://exploreflask.com/organizing.html

The template generated result can be found in [flask_sample_project][https://github.com/ericacheong/flask_sample_project]

## Generated file structure
```
\sample
    \config
        __init__.py
        default.py
        development.py
        production.py
    \instance
        config.py
    \sample
        \static
            style.css
        \templates
            index.html
            layout.html
            login.html
        __init__.py
        models.py
        views.py
    .gitignore
    runserver.py
    start.sh
```

## Language
- [Python][1]

## Prerequisite
- Python v2.7

## Usage instructions
1. Download file flask_project_creator.py
2. Run "python flask_project_creator.py my_app_name"

## Run project
1. Change the APP_CONFIG_FILE variable to the correct absolute path of config file in your system (default.py or development.py or production.py)
2. Chmod and make start.sh executable
```
$ chmod a+x start.sh
```
3. Run start.sh
```
$ ./start.sh
```


[1]: http://python.org