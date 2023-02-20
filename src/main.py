from flask import Flask, render_template
from apps.auth_app.views import auth_app
from apps.auth_app.models import User
from apps.articles.views import articles_app
from database import db_session
import os
from flask_login import LoginManager 


# create flask instance
app = Flask(__name__)
# secret key create
app.config['SECRET_KEY'] = os.urandom(24)

# User Manger
login_manager = LoginManager(app)

# define url of view login
# login_manager.login_view = "user_app.login_page"

# register blueprint
app.register_blueprint(auth_app)
app.register_blueprint(articles_app)

# User Loading Here
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# error pag
@app.errorhandler(404)
def error_handle(error):
    return render_template('error.html', error_message = error)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
    
if __name__ == '__main__':
    app.run(debug=True)
