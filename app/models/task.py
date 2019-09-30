from app import db
import json

class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    text = db.Column(db.String)

    def __repr__(self):
        return f"<Task(id={str(self.id)} title={self.title} text={self.text})"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "text": self.text
        }
