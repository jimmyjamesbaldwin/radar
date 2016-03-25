#!flask/bin/python
import sys

try:
	from app import app, db
	from flask.ext.script import Manager, prompt_bool
	from config import SQLALCHEMY_DATABASE_URI
	from config import SQLALCHEMY_MIGRATE_REPO
	from shutil import copyfile
	import os.path
	import datetime, time
except ImportError:
	print 'It looks like you don\'t have project dependencies. Install them by executing app/install.sh.'
	sys.exit(1)

manager = Manager(app)

@manager.command
def runserver():
	app.run(host='0.0.0.0')

@manager.command
def runserver_debug():
	app.run(host='0.0.0.0', debug=True)

@manager.command
def db_create():
	if os.path.exists(SQLALCHEMY_DATABASE_URI[10:]):
		print 'Database file already exists'
		return
	db.create_all()

@manager.command
def db_backup():
	timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
	copyfile('app.db', SQLALCHEMY_MIGRATE_REPO + '/versions/' + timestamp + '.db')

@manager.command
def db_drop():
	if prompt_bool("This operation will drop the database, continue?"):				
		db.drop_all()

@manager.command
def db_fill():
	if prompt_bool("Proceeding to fill the database with data. Continue?"):
		from app import fill_db
		fill_db.fill_her_up()


if __name__ == '__main__':
	manager.run()

