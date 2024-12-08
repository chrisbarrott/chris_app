import logging

from flask import Flask, jsonify, render_template, request
from services.database.database import CalEvent, db, init_db

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
init_db(app)

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

@app.route('/add_event', methods=['POST'])
def add_event():
    data = request.get_json()
    if not data or 'title' not in data or 'start' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    new_event = CalEvent(title=data['title'], start=data['start'], end=data.get('end'))
    try:
        db.session.add(new_event)
        db.session.commit()
        return jsonify({'message': 'Event added successfully'}), 201
    except Exception as e:
        print(f"Error adding event: {e}")
        db.session.rollback()
        return jsonify({'error': 'Database error'}), 500

@app.route('/get_events', methods=['GET'])
def get_events():
    try:
        events = CalEvent.query.all()
        events_list = [{'id': e.id, 'title': e.title, 'start': e.start, 'end': e.end} for e in events]
        return jsonify(events_list)
    except Exception as e:
        print(f"Error fetching events: {e}")
        return jsonify({'error': 'Database error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)

    
# @app.route('/get_events', methods=['GET'])
# def fetch_events():
#     return get_events()

# @app.route('/add_event', methods=['POST'])
# def add_event():
#     data = request.get_json()
#     return add_event_to_database(data)

