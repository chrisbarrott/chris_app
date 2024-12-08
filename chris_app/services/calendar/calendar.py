from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

# In-memory events (replace with DB logic for production)
events = [
    {'title': 'Event 1', 'start': '2024-12-10', 'end': '2024-12-12'},
    {'title': 'Event 2', 'start': '2024-12-15'},
]

def get_events():
    """Retrieve all events."""
    return jsonify(events)

def add_event(data):
    """Add a new event."""
    if not data or 'title' not in data or 'start' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    # Add event to the list
    new_event = {
        'title': data['title'],
        'start': data['start'],
        'end': data.get('end')  # Optional end date
    }
    events.append(new_event)
    return jsonify({'message': 'Event added successfully'})

"""
db = SQLAlchemy()

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    start = db.Column(db.String(10), nullable=False)
    end = db.Column(db.String(10), nullable=True)

def get_events():
    events = Event.query.all()
    return jsonify([{'title': e.title, 'start': e.start, 'end': e.end} for e in events])

def add_event(data):
    if not data or 'title' not in data or 'start' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    new_event = Event(title=data['title'], start=data['start'], end=data.get('end'))
    db.session.add(new_event)
    db.session.commit()
    return jsonify({'message': 'Event added successfully'})
"""