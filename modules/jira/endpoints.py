from fastapi import  APIRouter ,Request

from modules.jira.services.octo_api import Profile

router = APIRouter()

@router.post('/create')
async def create_profile(requests:Request):
    response = await requests.json()
    print(response)
    name = response['issue']['fields']['summary']
    tag = 'to_do'
    email = response['user']['emailAddress']
    response = Profile.create(name,tag)
    print(response)

@router.post('/move_to_warming')
async def move_to_warming(requests:Request):
    response = await requests.json()
    print(response)
    tag = response['issue']['fields']['status']['name']
    name = response['issue']['fields']['summary']
    print(tag,name)
    data = Profile.search_uuid(name)
    uuid = data['data'][0]['uuid']
    response = Profile.update_profile(uuid,tag)
    print(response)

@router.post('/move_to_register')
async def move_to_warming(requests:Request):
    response = await requests.json()
    tag = 'registr'
    name = response['issue']['fields']['summary']
    data = Profile.search_uuid(name)
    uuid = data['data'][0]['uuid']
    response = Profile.update_profile(uuid,tag)
    print(response)