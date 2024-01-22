from flask import Flask
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# SQLAlchemy configuration
DATABASE_URI = 'sqlite:///example.db'
engine = create_engine(DATABASE_URI, echo=True)  # Set echo to True for debugging
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Model declaration
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)

# Create tables
Base.metadata.create_all(engine)

# Perform database operations
user = User(username='example_user')
session.add(user)
session.commit()

# Query the database
all_users = session.query(User).all()