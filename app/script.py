import flask

app = flask(__name__)

@app.route('/')
@app.route('/index')
def hello():
    return flask.render_template('index.html')