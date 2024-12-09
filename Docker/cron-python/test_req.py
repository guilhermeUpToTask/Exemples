import requests

# Define the username whose information you want to retrieve
username = 'octocat'

# URL of the GitHub API endpoint for user information
url = f'https://api.github.com/users/{username}'

# Make a GET request to the API endpoint
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    user_data = response.json()

    # Print the user's information
    print(f"Username: {user_data['login']}")
    print(f"Name: {user_data['name']}")
    print(f"Bio: {user_data['bio']}")
    print(f"Followers: {user_data['followers']}")
    print(f"Following: {user_data['following']}")
else:
    print(f"Failed to fetch user data: {response.status_code}")
