import json
a = {"role":"commuting","material":"steel","ip":"128.0.0.1"}

with open('survey.json', 'w') as db:   
  json.dump(a,db)

