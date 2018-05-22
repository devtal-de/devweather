#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from webapp import app,db

manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.command
def bcryptbenchmark():
    "Test number of rounds"
    # Chance the number of rounds (second argument) until it takes between
    # 0.25 and 0.5 seconds to run.
    from flask.ext.bcrypt import generate_password_hash
    import time
    duration = 0
    i=4
    while duration < 0.25:
        start = time.time()
        generate_password_hash('password1', i)
        end = time.time()
        duration = end - start
        i += 1
    print( "(" + str(duration) + " secounds)")
    print( "please copy the next line into config.py")
    print( "")
    print( "BCRYPT_LOG_ROUNDS=" + str(i))

if __name__ == "__main__":
    app.debug = True
    manager.run()
