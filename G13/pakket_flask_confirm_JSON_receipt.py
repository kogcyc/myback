from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def process_post_data():
    try:
        # Get the JSON data from the request
        data = request.json

        # Process the data as needed (in this example, simply print it)
        print("Received data:", data)

        # Respond with a JSON message
        return jsonify({'message': 'Data received successfully'}), 200

    except Exception as e:
        # Handle any errors that may occur during processing
        print("Error processing data:", str(e))
        return jsonify({'error': 'An error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)