from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate
from info import current_app, db

import models

app = current_app()
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()