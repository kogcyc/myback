import requests
import base64

github_token = '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'
repo_owner = 'kogcyc'
repo_name = 'files'
branch_name = 'main'
file_name = 'aaaaa_hello'

content = 'hellooooo'
content_base64 = base64.b64encode(content.encode()).decode('utf-8')

api_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_name}'
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