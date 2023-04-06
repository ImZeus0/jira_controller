from fastapi import  APIRouter ,Request
from modules.github.service.create import create_repo
router = APIRouter()

@router.post('/create_repo')
async def create_repo(request:Request):
    request = request.json()
    namedValue = request['fields']['issuetype']['namedValue']
    if namedValue == 'Story':
        name = request['key']
    response = create_repo(name)
    print(response)
    return response