from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Get file information from the request
    file = request.files['file']
    file_name = file.filename

    # Save the file locally (or process as needed)
    file.save(os.path.join("uploads", file_name))

    # GitHub API details
    github_token = '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'
    repo_owner = 'kogcyc@gmail.com'
    repo_name = 'files'
    branch_name = 'main'

    # GitHub API endpoint for creating a new file
    api_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_name}'

    # Read the content of the file
    with open(os.path.join("uploads", file_name), 'rb') as file_content:
        content_base64 = base64.b64encode(file_content.read()).decode('utf-8')

    # Create a commit using the GitHub API
    headers = {
        'Authorization': f'Bearer {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    data = {
        'message': f'Add {file_name}',
        'content': content_base64,
        'branch': branch_name
    }

    response = requests.put(api_url, headers=headers, json=data)

    if response.status_code == 201:
        return 'File added to GitHub repository!'
    else:
        return 'Failed to add file to GitHub repository.'

if __name__ == '__main__':
    app.run(debug=True)
