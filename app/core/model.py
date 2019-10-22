from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func as util

model = SQLAlchemy()


class User(model.Model):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    fullname = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def create_journal(self, title):
        journal = Journal(title=title, user_id=self.id)
        model.session.add(journal)
        model.session.commit()


class Journal(model.Model):
    __tablename__ = "journal"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, unique=True)

    user = model.relationship("User", back_populates="journal")

    def create_entry(self, title, body):
        entry = Entry(title=title, body=body, journal_id=self.id)
        model.session.add(entry)
        model.session.commit()


class Entry(model.Model):
    __tablename__ = "entry"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)
    journal_id = Column(Integer, ForeignKey('journal.id'), nullable=False)
    time_created = Column(DateTime, nullable=False, server_default=util.now())

    journal = model.relationship("Journal", back_populates="entry")
