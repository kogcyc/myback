from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Serve the survey.html file
@app.route('/')
def index():
    return render_template('survey.html')

# Process the form data and return a JSON object
@app.route('/surveyProcess', methods=['POST'])
def survey_process():
    data = request.form.to_dict()
    data['ip_address'] = request.remote_addr
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

