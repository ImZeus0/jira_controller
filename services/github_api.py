import base64
import os.path

import requests
from core.config import get_settings

HEADERS = {
         'Authorization': f'Bearer {get_settings().git_hub_token}',
         'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }
def create_repo(name):
    github_api_url = 'https://api.github.com/user/repos'
    data = {
        "name": name,
        "private": True,
    }
    response = requests.post(github_api_url, headers=HEADERS, json=data)
    if response.status_code == 201:
        print(f"Repository {name} created successfully.")
        return response.json()['clone_url']
    elif response.status_code == 422:
        print(f"Repository {name} already exists.")
        return 422
    else:
        print(f"Failed to create repository {name}. Status code: {response.status_code} {response.text} {response.request.body}")
        return None

def add_file_action(repo):
    path = '.github/workflows/test_app.yml'
    url = f"https://api.github.com/repos/{get_settings().git_hub_user}/{repo}/contents/{path}"
    content = base64.b64encode(open(os.getcwd()+'/services/example_action.txt','rb').read()).decode()
    print(content)
    params = {
        "message": "Add test_app.yml",
        "content": content,
        "path": path
    }
    response = requests.put(url, headers=HEADERS, json=params)
    print(response.status_code,response.json())

def add_webhook(repo):
    url = f"https://api.github.com/repos/{get_settings().git_hub_user}/{repo}/hooks"
    params = {
              "name": "web",
              "active": True,
              "events": [
                "workflow_run_completed"
              ],
              "config": {
                "url": "https://jira.adstools.net/applications/finish_action",
                "content_type": "json",
                "secret": "your-webhook-secret"
              }
            }
    response = requests.post(url, headers=HEADERS, json=params)
    print(response.status_code,response.text)


def send_collaborators(repo,to_user):
    url = f'https://api.github.com/repos/{get_settings().git_hub_user}/{repo}/collaborators/{to_user}'
    print(url)
    data = {"permission":"admin"}
    response = requests.put(url,headers=HEADERS,json=data)
    print(response.status_code,response.text)

def run_action(repo,workflow_id):
    url = f'https://api.github.com/repos/{get_settings().git_hub_user}/{repo}/actions/runs/{workflow_id}/rerun'
    HEADERS = {
        'Authorization': f'Bearer {get_settings().git_hub_token}',
        'Accept': 'application/vnd.github.v3+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    response = requests.post(url,headers=HEADERS)
    print(response.status_code,response.text)

def show_result_action(repo,run_id):
    url = f'https://api.github.com/repos/{get_settings().git_hub_user}/{repo}/actions/runs/{run_id}'
    response_run = requests.get(url, headers=HEADERS).json()
    if response_run.get('conclusion') == 'success':
        headers = {
            'Authorization': f'Bearer {get_settings().git_hub_token}',
            #'Accept': 'application/vnd.github.v3+json',
            'accept-encoding':'identify',
            'X-GitHub-Api-Version': '2022-11-28'
        }
        response_log = requests.get(response_run['logs_url'],headers=headers).content
        with open('111.zip','wb') as writer:
            writer.write(response_log)
    else:
        print(response_run)


