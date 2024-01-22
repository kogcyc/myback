
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# SQLAlchemy configuration
#DATABASE_URI = 'sqlite:///example.db'
DATABASE_URI = 'mysql+pymysql://matt:kikikiki@raspberrypi.local/matt'
engine = create_engine(DATABASE_URI, echo=False)  # Set echo to True for debugging
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Model declaration
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)

# Create tables
#Base.metadata.create_all(engine)

# Perform database operations
#user = User(username='someone_else')
#session.add(user)
#session.commit()

# Query the database
all_users = session.query(User).all()