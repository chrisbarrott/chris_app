from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Declare a basic calender event
class CalEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    start = db.Column(db.String(10), nullable=False)
    end = db.Column(db.String(10), nullable=True)

# Initialize the database with the Flask app
def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

# Delete a cal event from the database by ID
def delete_event_from_database(event_id):
    try:
        event = CalEvent.query.get(event_id)
        if not event:
            return False, "Event not found"
        
        db.session.delete(event)
        db.session.commit()
        return True, "Event deleted successfully"
    
    except Exception as e:
        print(f"Error deleting event: {e}")
        db.session.rollback()
        return False, "Database error"

# Add a new calender event to the database
def add_event_to_database(data):
    print(f"Received event data: {data}")
    if not data or 'title' not in data or 'start' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    new_event = CalEvent(title=data['title'], start=data['start'], end=data.get('end'))
    try:
        db.session.add(new_event)
        db.session.commit()
        print(f"Adding event: {new_event}")
        return jsonify({'message': 'Event added successfully'}), 201
    
    except Exception as e:
        print(f"Error adding event: {e}")
        db.session.rollback()
        return jsonify({'error': 'Database error'}), 500

# Fetch all events from the database.
def get_events_from_database():
    try:
        print(f"Getting events")
        events = CalEvent.query.all()
        events_list = [{'id': e.id, 'title': e.title, 'start': e.start, 'end': e.end} for e in events]
        print(f"Events: {events_list}")
        return True, events_list
    
    except Exception as e:
        print(f"Error fetching events: {e}")
        return jsonify({'error': 'Database error'}), 500