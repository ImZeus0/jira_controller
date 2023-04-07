from fastapi import  APIRouter ,Request
from services.github_api import create_repo,add_file_action
router = APIRouter()

@router.post('/create_repo')
async def create_repo_mentod(request:Request):
    request = await request.json()
    namedValue = request['fields']['issuetype']['namedValue']
    summary = request['fields']['summary']
    print(namedValue,summary)
    if namedValue == 'Sub-task' and summary == 'app':
        name = request['key']
        create_repo(name)
        add_file_action(name)
@router.post('/finish_action')
async def finish_action(request:Request):
    request = await request.json()
    print(request)

