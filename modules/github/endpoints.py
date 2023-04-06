from fastapi import  APIRouter ,Request
from service.create import create
router = APIRouter()

@router.post('/create_repo')
async def create_repo(request:Request):
    request = request.json()
    namedValue = request['fields']['issuetype']['namedValue']
    if namedValue == 'Story':
        name = request['key']
    response = create(name)
    print(response)
    return response