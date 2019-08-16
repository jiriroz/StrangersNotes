from app import db

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    title = db.Column(db.String(64))
    body = db.Column(db.String(512))

    def __repr__(self):
        return "note id: {}, username: {}, note title: {}".format(self.id, self.username, self.title)
