import json
a = {"127.0.0.1": {"Role": "commuting", "Material": "steel-fillet"}}

with open('survey.json', 'w') as db:   
  json.dump(a,db)

