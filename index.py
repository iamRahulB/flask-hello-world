from flask import Flask, render_template
from second import second_app

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

app.register_blueprint(second_app)

if __name__ == '__main__':
    app.run()
