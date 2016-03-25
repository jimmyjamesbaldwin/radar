RADAR
=====

Room Availability Detection and Reconnaissance.  
A room availability display for BU Computing.

Intro
-----
A simple web app which shows which rooms in Poole house aren't currently
in use. Frontend created by drawing SVG's, backend created with Flask/SQLAlchemy.

Basic Usage
-----
A python script 'manage.py' in the root of the repo is used to control the application.
It can be used to start/stop the web server, create the database, populate data, etc.

To get started, start a terminal and 'cd' into the correct directory, then run:
```
python ./manage.py
```

The app may prompt to install dependencies, which can be done with the following
command:
```
sudo app/deploy/install.sh
```

Executing manage.py will show a list of options. To start the web server type:
```
python ./manage.py runserver
```
...and it will start on 127.0.0.1:5000.

Requirements
------------
The app should run on any machine with python. The dependency install script (app/deploy/install.sh) should handle everything.

Contributors
------------
Contributers are welcome. Feel free to make a pull request, although ensure any
changes are sustainable for future use of the application without major user interaction.

Authors
-------
Frontend Dev: David Bain [web][web_bain]  
Backend Dev:  Jimmy [web][web_jimmy]


[web_bain]: http://davidba.in
[web_jimmy]: https://jamesbaldwin.co.uk
