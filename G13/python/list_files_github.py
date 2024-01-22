#curl -H "Authorization: Bearer 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" https://api.github.com/repos/kogcyc/files/contents/

#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


import requests

# Replace these with your GitHub credentials
github_username = "kogcyc"
github_token = "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"

# Replace with the repository owner, repository name, and directory path
owner = "kogcyc"
repo = "book1"
path = ""  # Use an empty string for the root directory

# Construct the URL for the API request
url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"

# Set up the request headers with the Authorization header
headers = {
    "Authorization": f"Bearer {github_token}"
}

# Make the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    content_list = response.json()
    
    # Iterate through the contents and print them
    for item in content_list:
        print(f"Name: {item['name']}, Type: {item['type']}")

else:
    print(f"Failed to retrieve contents. Status code: {response.status_code}")
