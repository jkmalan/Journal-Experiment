from sqlalchemy import Column, Boolean, Integer, Numeric, String, DateTime, ForeignKey

from app.core import db, bc, lm


class Base(db.Model):
    __abstract__ = True
    created_on = Column(DateTime, default=db.func.now())
    updated_on = Column(DateTime, default=db.func.now(), onupdate=db.func.now())

    def create(self):
        db.session.add(self)
        db.session.commit()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    fullname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    @property
    def is_authenticated(self):
        return True

    def get_id(self):
        return self.id

    def store_password(self, password):
        self.password = bc.generate_password_hash(password).decode('UTF-8')

    def match_password(self, password):
        return bc.check_password_hash(self.password, password=password)

    def get_journal(self):
        journal = Journal.query.filter_by(user_id=self.id).first()
        return journal

    def create_journal(self, title):
        journal = Journal(title=title, user_id=self.id)
        db.session.add(journal)
        db.session.commit()


@lm.user_loader
def load_user(id):
    if isinstance(id, int):
        pass
    elif isinstance(id, str):
        if id.strip().isdigit():
            id = int(id)
        else:
            return
    else:
        return

    return User.query.get(id)


class Journal(Base):
    __tablename__ = "journal"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, unique=True)
    user = db.relationship("User", backref="user", foreign_keys=[user_id])

    def get_entries(self):
        entry = Entry.query.filter_by(journal_id=self.id).all()
        return entry

    def add_entry(self, title, body):
        entry = Entry(title=title, body=body, journal_id=self.id)
        db.session.add(entry)
        db.session.commit()


class Entry(Base):
    __tablename__ = "entry"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)

    journal_id = Column(Integer, ForeignKey('journal.id'), nullable=False)
    journal = db.relationship("Journal", backref="journal", foreign_keys=[journal_id])

    def get_emotions(self):
        emotion = Emotion.query.filter_by(entry_id=self.id).all()
        return emotion

    def add_emotion(self, name, value):
        emotion = Emotion(name=name, value=value, entry_id=self.id)
        db.session.add(emotion)
        db.session.commit()


class Emotion(db.Model):
    __tablename__ = "emotion"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(Numeric(12, 8))

    entry_id = Column(Integer, ForeignKey('entry.id'), nullable=False)
    entry = db.relationship("Entry", backref="entry", foreign_keys=[entry_id])
