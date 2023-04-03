from fastapi import  APIRouter ,Request

from modules.jira.services.octo_api import Profile

router = APIRouter()

@router.post('/create')
async def create_profile(requests:Request):
    response = await requests.json()
    name = response['fields']['summary']
    tag = 'TO DO'
    email = response['user']['email']
    response = Profile.create(name,tag)
    print(response)

@router.post('/move_to_warming')
async def move_to_warming(requests:Request):
    response = await requests.json()
    tag = response['filelds']['status']['name']
    name = response['fields']['summary']
    data = Profile.search_uuid(name)
    uuid = data['data'][0]['uuid']
    response = Profile.update_profile(uuid,tag)
    print(response)

