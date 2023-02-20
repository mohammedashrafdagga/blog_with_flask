from flask import Blueprint
from flask import render_template

# articles_app blue print
articles_app = Blueprint('articles', __name__, url_prefix = '/', )


# home page
@articles_app.route('/')
def homepage():
    return render_template('base.html')