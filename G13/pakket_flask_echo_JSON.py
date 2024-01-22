from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/pakket/echoJSON', methods=['POST'])
def echoJSON():
    try:
        data = request.json  # This is a dictionary containing the JSON data
        print("Received JSON data:", data)

        # Echo the received JSON back to the requestor
        data['firstName'] = None
        return jsonify(data), 200

    except Exception as e:
        print("Error processing data:", str(e))
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
