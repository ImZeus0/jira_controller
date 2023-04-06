import requests
from core.config import get_settings


def create_repo(name):
    github_token = get_settings().git_hub_token
    github_api_url = 'https://api.github.com/user/repos'

    headers = {
         'Authorization': f'Bearer {github_token}',
         'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    data = {
        "name": name,
        "private": True,
    }
    response = requests.post(github_api_url, headers=headers, json=data)
    if response.status_code == 201:
        print(f"Repository {name} created successfully.")
        return response.json()['clone_url']
    elif response.status_code == 422:
        print(f"Repository {name} already exists.")
        return 422
    else:
        print(f"Failed to create repository {name}. Status code: {response.status_code} {response.text} {response.request.body}")
        return None
