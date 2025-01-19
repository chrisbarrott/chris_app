document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        events: '/get_events', // Fetch events from your API
        eventContent: function(arg) {
            // Customize event content here
            return { html: `<b>${arg.event.title}</b>` }; // Example: Display title in bold
        },
        eventClick: function(info) {
            // Handle event click (for example, you could display more details or delete the event)
            alert('Event: ' + info.event.title);
        },
        editable: true, // Allow user interactions
        eventClick: function (info) {
            if (confirm(`Delete the event "${info.event.title}"?`)) {
                fetch(`/delete_event/${info.event.id}`, {
                    method: 'DELETE',
                })
                .then(response => {
                    if (response.ok) {
                        alert('Event deleted successfully!');
                        calendar.refetchEvents(); // Reload events
                    } else {
                        response.json().then(data => alert(`Error: ${data.error}`));
                    }
                })
                .catch(error => console.error('Error:', error));
            }
        }
    });

    calendar.render();

    // Handle Add Event Form Submission
    document.getElementById('addEventForm').addEventListener('submit', function (e) {
        e.preventDefault();

        const title = document.getElementById('eventTitle').value;
        const start = document.getElementById('eventStart').value;
        const end = document.getElementById('eventEnd').value;

        fetch('/add_event', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title, start, end }),
        })
        .then(response => {
            if (response.ok) {
                alert('Event added successfully!');
                document.getElementById('addEventForm').reset(); // Reset form
                const modalCloseButton = document.querySelector('#addEventModal .btn-close');
                modalCloseButton.click(); // Close modal
                calendar.refetchEvents(); // Reload events
            } else {
                response.json().then(data => alert(`Error: ${data.error}`));
            }
        })
        .catch(error => console.error('Error:', error));
    });
});