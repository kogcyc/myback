from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# Define the model
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

# Create an in-memory SQLite database engine
engine = create_engine('sqlite:///:memory:', echo=True)

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Add a user to the database
new_user = User(name='John Doe', age=30)
session.add(new_user)
session.commit()

# Query the database to retrieve the user
queried_user = session.query(User).filter_by(name='John Doe').first()
print(f"Queried User: {queried_user.name}, Age: {queried_user.age}")

# Close the session
session.close()


