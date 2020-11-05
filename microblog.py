from app import app,db
from app.models import User, Post

app.config['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}