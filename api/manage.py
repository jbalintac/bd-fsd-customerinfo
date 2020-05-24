import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_cors import cross_origin

# Note: Need to import to fix werkzeug bug
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

from app import blueprint
from app.main import create_app, db

app = create_app(os.getenv('ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    manager.run()