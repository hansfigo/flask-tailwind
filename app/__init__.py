from flask import Flask, render_template
from app.routes import wife_blueprint, home_blueprint


def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(wife_blueprint, url_prefix="/wife")
    app.register_blueprint(home_blueprint, url_prefix="/")

    @app.route("/about")
    def about():
        return render_template('about.html', page="About")
    
    return app
