from sqlalchemy import create_engine, Column, Integer, String, Sequence, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import rich

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import rich

# Define the model
Base = declarative_base()

class Survey(Base):
    __tablename__ = 'survey'
    ip = Column(String(20), primary_key=True)
    role = Column(String(40))
    material = Column(String(40))
    framesize = Column(String(40))
    wheelsize = Column(String(40))
    other = Column(String(255))

# Create an in-memory SQLite database engine
engine = create_engine('sqlite:///:memory:', echo=False)

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Add a user to the database
survey_item = Survey(ip='192.168.1.22', role="commuting", material="steel-tig", framesize="57", wheelsize="27.5", other="hello")
session.add(survey_item)
survey_item = Survey(ip='129.44.112.1', role="commuting", material="aluminum-tig", framesize="57", wheelsize="27.5", other="")
session.add(survey_item)
session.commit()

#..................................................................................

# Query all records and iterate through them
all_survey_records = session.query(Survey).all()

# Print the queried records
for record in all_survey_records:
    print(f"IP: {record.ip}, Material: {record.material}")

#..................................................................................

# Query all columns using raw SQL query
sql_query = text("SELECT * FROM survey")

result = session.execute(sql_query)

print(rich.inspect(result,all=all))

# Fetch and print the queried records
for row in result:
    print(f"IP: {row[0]}, Material: {row[1]}")
    #print(rich.inspect(row,all=all))

#..................................................................................


# Close the session
session.close()



@app.route('/json', methods = ['GET'])
def json():
    data = {"world":"hello"}
    return jsonify(data)

#@app.route('/survey')
#def survey():
#    survey = Survey.query.all()
#    #return render_template('survey.html', survey=survey)
#    return rich.inspect(survey,all=all)

@app.route('/survey')
def survey():
    retsurvey = Survey.query.all()
    survey_string = "\n".join([f"Survey IP: {survey.ip}, Material: {survey.material}, Framesize: {survey.framesize}" for survey in retsurvey])
    return render_template('survey.html', survey_string=survey_string)

if __name__ == "__main__":
    app.run(debug=True)


