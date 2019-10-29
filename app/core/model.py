from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Numeric, String, DateTime, ForeignKey

model = SQLAlchemy()


class Base(model.Model):
    __abstract__ = True
    created_on = Column(DateTime, default=model.func.now())
    updated_on = Column(DateTime, default=model.func.now(), onupdate=model.func.now())


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    fullname = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def get_journal(self):
        journal = Journal.query.filter_by(user_id=self.id).first()
        return journal

    def create_journal(self, title):
        journal = Journal(title=title, user_id=self.id)
        model.session.add(journal)
        model.session.commit()


class Journal(Base):
    __tablename__ = "journal"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, unique=True)
    user = model.relationship("User", backref="user", foreign_keys=[user_id])

    def get_entries(self):
        entry = Entry.query.filter_by(journal_id=self.id).all()
        return entry

    def add_entry(self, title, body):
        entry = Entry(title=title, body=body, journal_id=self.id)
        model.session.add(entry)
        model.session.commit()


class Entry(Base):
    __tablename__ = "entry"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)

    journal_id = Column(Integer, ForeignKey('journal.id'), nullable=False)
    journal = model.relationship("Journal", backref="journal", foreign_keys=[journal_id])

    def get_emotions(self):
        emotion = Emotion.query.filter_by(entry_id=self.id).all()
        return emotion

    def add_emotion(self, name, value):
        emotion = Emotion(name=name, value=value, entry_id=self.id)
        model.session.add(emotion)
        model.session.commit()


class Emotion(model.Model):
    __tablename__ = "emotion"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(Numeric(12, 8))

    entry_id = Column(Integer, ForeignKey('entry.id'), nullable=False)
    entry = model.relationship("Entry", backref="entry", foreign_keys=[entry_id])
