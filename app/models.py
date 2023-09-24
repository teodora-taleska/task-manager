# models.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URI
from sqlalchemy.orm import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash

# Create a SQLAlchemy engine using the DATABASE_URI
engine = create_engine(DATABASE_URI)

# Create a session factory
Session = sessionmaker(bind=engine)
session = Session()

# Define your SQLAlchemy models and use the engine and Session as needed
Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    uid = Column(Integer, primary_key=True)
    name = Column(String(100))
    surname = Column(String(100))
    email = Column(String(200), unique=True)
    password = Column(String(300))

    def __init__(self, name, surname, email, user_pass):
        self.name = name
        self.surname = surname
        self.email = email
        self.set_pass(user_pass)

    def __repr__(self):
        return f"{self.uid}: {self.name} {self.surname} ... pass: {self.password}"

    def set_pass(self, user_pass):
        self.password = generate_password_hash(user_pass)

    def check_pass(self, user_pass):
        return check_password_hash(self.password, user_pass)

    @classmethod
    def email_exists(cls, session, email):
        # Use a query to check if a user with the provided email exists in the database
        existing_user = session.query(cls).filter_by(email=email).first()
        return existing_user is not None


class Tasks(Base):
    __tablename__ = 'tasks'

    tid = Column(Integer, primary_key=True)
    status = Column(String(100))
    category = Column(String(100))
    name = Column(String(100))
    date = Column(DateTime, default=func.current_timestamp())
    deadline = Column(DateTime)
    priority = Column(Integer)
    userId = Column(Integer, ForeignKey("users.uid"))

    def __init__(self, status, category, name, deadline, priority, userId):
        self.tid = None
        self.status = status
        self.category = category
        self.name = name
        self.deadline = deadline
        self.priority = priority
        self.userId = userId

    def __repr__(self):
        return f"Task id: {self.tid} \n" \
               f"Task: {self.name} \n" \
               f"Category: {self.category} \n" \
               f"Created on: {self.date} \n" \
               f"Status: {self.status} \n" \
               f"Priority: {self.priority} \n" \
               f"Deadline: {self.deadline} \n"


Base.metadata.create_all(engine)
