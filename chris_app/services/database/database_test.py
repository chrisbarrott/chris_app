from chris_app.services.database.database import db, CalEvent  

with db.app_context():
    db.create_all()
    try:
        test_event = CalEvent(title="Test Event", start="2024-12-08", end="2024-12-09")
        db.session.add(test_event)
        db.session.commit()
        print("Event added successfully!")
    except Exception as e:
        print(f"Database error: {e}")
