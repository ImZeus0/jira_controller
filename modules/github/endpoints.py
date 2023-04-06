from fastapi import  APIRouter ,Request
from modules.github.service.create import create_repo
router = APIRouter()

@router.post('/create_repo')
async def create_repo(request:Request):
    request = await request.json()
    namedValue = request['fields']['issuetype']['namedValue']
    summary = request['fields']['summary']
    print(namedValue,summary)
    if namedValue == 'Sub-task' and summary == 'app':
        name = request['key']
        response = create_repo(name)
        print(response)
