from flask import blueprints,render_template

home_blueprint = blueprints.Blueprint('home', __name__)

@home_blueprint.route("/")
def home():
    return render_template('home.html', page="Home")
