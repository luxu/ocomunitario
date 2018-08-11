import os
from app import create_app, db
from app.controllers.auth.model import Account
from flask_migrate import Migrate


app = create_app(os.environ.get('FLASK_MODE') or 'default')

# Migrate Instance
Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, Account=Account)
