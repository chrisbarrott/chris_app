import logging

from datetime import datetime
from flask import Flask, jsonify, render_template, request
from services.search.search import search_dashboards
from services.database.database import CalEvent, db, delete_event_from_database, init_db, add_event_to_database, get_events_from_database

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

@app.route('/search', methods=['GET'])
def search_page():
    return render_template('search.html')

@app.route('/get_events', methods=['GET'])
def get_events():
    success, message = get_events_from_database()
    if success:
        return jsonify({'message': message}), 200
    else:
        return jsonify({'error': message}), 400

@app.route('/add_event', methods=['POST'])
def add_event():
    data = request.get_json()
    success, message = add_event_to_database(data)
    if success:
        return jsonify({'message': message}), 200
    else:
        return jsonify({'error': message}), 400

@app.route('/delete_event/<int:event_id>', methods=['DELETE'])
def delete_event_route(event_id):
    success, message = delete_event_from_database(event_id)
    if success:
        return jsonify({'message': message}), 200
    else:
        return jsonify({'error': message}), 400

def format_event_dates(events):
    for event in events:
        # Ensure the start and end have time in the format 'YYYY-MM-DDTHH:MM:SS'
        event['start'] = f"{event['start']}T00:00:00"  # Default to midnight
        event['end'] = f"{event['end']}T23:59:59"  # Default end time to 23:59:59
    return events

@app.route('/search_dashboard', methods=['GET'])
def search_dashboard():
    query = request.args.get('q', '')
    results = search_dashboards(query)
    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
