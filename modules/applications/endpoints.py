import os

from fastapi import  APIRouter ,Request
from services.github_api import create_repo,add_file_action
from core.config import get_settings
router = APIRouter()

@router.post('/create_repo')
async def create_repo_mentod(request:Request):
    request = await request.json()
    print(request)
    email = request['fields']['assignee']['emailAddress']
    namedValue = request['fields']['issuetype']['namedValue']
    summary = request['fields']['summary']
    print(namedValue,summary)
    if namedValue == 'Sub-task' and summary == 'app':
        name = request['key']
        create_repo(name)
        add_file_action(name)

@router.post('/move_to_qa')
async def move_to_ready(request:Request):
    request = await request.json()
    print(request)
    key = request['key']
    clone_url = f'https://{get_settings().git_hub_user}@github.com/{get_settings().git_hub_user}/{key}.git'
    os.system(f'cd repos && git clone {clone_url}')
    print(key)
@router.post('/finish_action')
async def finish_action(request:Request):
    request = await request.json()
    if request['workflow_run']['status'] == 'completed':
        issue_key = request['workflow_run']['repository']['name']


