from flask import Flask, request, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Parse the form data from the POST request payload
        form_data = {key: value for key, value in request.form.items()}
        
        # Process the form data as needed
        # In this example, we're simply returning the received data as JSON

        addr = request.remote_addr

        with open('survey.json', 'r') as f:
                b = json.load(f)
        b[f'{addr}'] = form_data
        with open('survey.json', 'w') as f:
                json.dump(b,f)

        return jsonify(form_data)

    return render_template('survey.html')

if __name__ == '__main__':
    app.run(debug=True)


