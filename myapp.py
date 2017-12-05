from flask import Flask
from flask import render_template
#app = Flask(__name__)
#app = Flask(__name__, instance_path='/root/flask/flask_test/instance/')
#app.config.from_pyfile('instance/settings.cfg')
app = Flask(__name__, instance_relative_config=True)
@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
