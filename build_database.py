from datetime import datetime
from src.config import app, db
from src.models import Person, Note

PEOPLE_NOTES = [
    {
        "fname": "Fallen",
        "lname": "Gabriel",
        "notes": [
            ("Today's match was intense!", "2023-12-02 12:30:00"),
            ("Practiced some new strategies with the team.", "2023-12-02 15:45:00"),
            ("Excited for the upcoming tournament!", "2023-12-02 18:00:00"),
        ],
    },
    {
        "fname": "Kogos",
        "lname": "Paulo",
        "notes": [
            ("Started a new gaming stream today.", "2023-12-02 10:00:00"),
            ("Reached a new high score in the latest game.", "2023-12-02 14:20:00"),
            ("Planning a collaboration with other streamers.", "2023-12-02 17:30:00"),
        ],
    },
    {
        "fname": "Alexandre",
        "lname": "Gaules",
        "notes": [
            ("Reflecting on the journey in the gaming industry.", "2023-12-02 08:45:00"),
            ("Grateful for the support from the community.", "2023-12-02 12:15:00"),
            ("Sharing thoughts on the future of esports.", "2023-12-02 16:40:00"),
        ],
    },
    {
        "fname": "Monark",
        "lname": "Brasil",
        "notes": [
            ("Working on exciting new projects for the channel.", "2023-12-02 11:30:00"),
            ("Discussing current events and trends with the audience.", "2023-12-02 14:55:00"),
            ("Appreciating the creativity of the community.", "2023-12-02 20:00:00"),
        ],
    },
]

with app.app_context():
    db.drop_all()
    db.create_all()
    for data in PEOPLE_NOTES:
        new_person = Person(lname=data.get("lname"), fname=data.get("fname"))
        for content, timestamp in data.get("notes", []):
            new_person.notes.append(
                Note(
                    content=content,
                    timestamp=datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"),
                )
            )
        db.session.add(new_person)
    db.session.commit()