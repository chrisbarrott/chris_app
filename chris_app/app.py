import logging

from flask import Flask, jsonify, render_template, request
from services.calendar.calendar import add_event, get_events, db

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    app.logger.debug('Home route was accessed')
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')
@app.route('/get_events', methods=['GET'])
def fetch_events():
    return get_events()

@app.route('/add_event', methods=['POST'])
def create_event():
    data = request.get_json()
    return add_event(data)

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)