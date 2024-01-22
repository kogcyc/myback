
from jinja2 import Template
import json

# Your JSON data
json_data = '''
{
  "groups": [
    {
      "name": "role",
      "options": [
        {"value": "Commuting", "label": "Commuting"},
        {"value": "Road", "label": "Road"},
        {"value": "Gravel", "label": "Gravel"}
      ]
    },
    {
      "name": "material",
      "options": [
        {"value": "Steel TIG'd", "label": "Steel, TIG'd"},
        {"value": "Steel fillet brazed", "label": "Steel, fillet brazed"},
        {"value": "Steel lugged", "label": "Steel, lugged"},
        {"value": "Aluminum TIG'd", "label": "Aluminum, TIG'd"}
      ]
    },
    {
      "name": "framesize",
      "options": [
        {"value": "53", "label": "53cm"},
        {"value": "55", "label": "55cm"},
        {"value": "57", "label": "57cm"},
        {"value": "59", "label": "59cm"},
        {"value": "61", "label": "61cm"}
      ]
    },
    {
      "name": "wheelsize",
      "options": [
        {"value": "29", "label": "29 (700C)"},
        {"value": "27.5", "label": "27.5 (650B)"},
        {"value": "26", "label": "26 (MTB 559)"}
      ]
    }
  ]
}
'''

# Load JSON data
data = json.loads(json_data)

# Jinja2 template
template_str = '''
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Radio Buttons Example</title>
</head>
<body>

<form action="http://localhost:5000" method="post" id="myForm">

  {% for group in groups %}
    <fieldset>
      <legend>{{ group.name }}</legend>
      {% for option in group.options %}
        <label>
          <input type="radio" name="{{ group.name }}" value="{{ option.value }}">
          {{ option.label }}
        </label><br>
      {% endfor %}
    </fieldset>
  {% endfor %}
  <input type="submit" value="Submit">

</form>

</body>
</html>
'''

# Create a Jinja2 template
template = Template(template_str)

# Render the template with the JSON data
html_output = template.render(groups=data['groups'])

# Output the HTML
print(html_output)
