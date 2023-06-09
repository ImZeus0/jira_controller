from fastapi import  APIRouter ,Request

from services.octo_api import Profile

router = APIRouter()

@router.post('/create')
async def create_profile(requests:Request):
    response = await requests.json()
    name = response['issue']['fields']['summary']
    tag = 'to_do'
    proxy = response['issue']['fields']['description']
    response = Profile.create(name,tag,proxy)
    print(response)

@router.post('/move_to_warming')
async def move_to_warming(requests:Request):
    response = await requests.json()
    tag = 'warning'
    name = response['fields']['summary']
    data = Profile.search_uuid(name)
    uuid = data['data'][0]['uuid']
    response = Profile.update_profile(uuid,tag)
    print(response)

@router.post('/move_to_register')
async def move_to_register(requests:Request):
    response = await requests.json()
    tag = 'registr'
    name = response['fields']['summary']
    data = Profile.search_uuid(name)
    uuid = data['data'][0]['uuid']
    response = Profile.update_profile(uuid,tag)
    print(response)