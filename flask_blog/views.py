from flask_blog import app
from flask import render_template
@app.route("/")
def index():
    return render_template('entries/index.html')
