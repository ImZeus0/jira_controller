import json
import requests
from core.config import get_settings

HEADERS = {'X-Octo-Api-Token': get_settings().token_octo, 'Content-Type': 'application/json'}
BASE_URL = 'https://app.octobrowser.net/api/v2/automation'

BASE_CONFIG_PROFILE = {
            "title": "Test profile from api",
            "description": "test description",
            "start_pages": ["https://fb.com"],
            "tags": [
                "to_do"
            ],
            "storage_options": {
                "cookies": True,
                "passwords": True,
                "extensions": True,
                "localstorage": True,
                "history": True,
                "bookmarks": True
            },
            "extensions": [],
            "fingerprint": {
                "os": "win",
                "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
                "screen": "1920x1080",
                "languages": {
                    "type": "ip"
                },
                "timezone": {
                    "type": "ip"
                },
                "geolocation": {
                    "type": "ip"
                },
                "cpu": 4,
                "ram": 8,
                "noise": {
                    "webgl": True,
                    "canvas": True,
                    "audio": True,
                    "client_rects": True
                },
                "webrtc": {
                    "type": "ip"
                },
                "dns": "1.1.1.1",
                "media_devices": {
                    "video_in": 1,
                    "audio_in": 1,
                    "audio_out": 1
                }
            }
        }

ERROR_FAILED_GET_IP = 4

class Profile:
    @classmethod
    def create(cls,name,tag,proxy=None):
        url = BASE_URL + '/profiles'
        BASE_CONFIG_PROFILE['title'] = name
        BASE_CONFIG_PROFILE['tags'] = [tag]
        if proxy is not None:
            proxy_config = {}
            connect_info = proxy.split(':')
            if len(connect_info) == 2:
                proxy_config['type'] = 'socks5'
                proxy_config['host'] = connect_info[0]
                proxy_config['port'] = connect_info[1]
            elif len(connect_info) == 4:
                proxy_config['type'] = 'socks5'
                proxy_config['host'] = connect_info[0]
                proxy_config['port'] = connect_info[1]
                proxy_config['login'] = connect_info[2]
                proxy_config['password'] = connect_info[3]
            else :
                uuid = cls.get_proxy(proxy)
                proxy_config['uuid'] = uuid
            BASE_CONFIG_PROFILE['proxy'] = proxy_config
        data = json.dumps(BASE_CONFIG_PROFILE)
        response = requests.post(url=url, data=data, headers=HEADERS)
        response = response.json()
        print(response)
        if response.get('success'):
            return response['data']['uuid']
        else:
            return response.get('msg')

    @classmethod
    def search_uuid(cls,name):
        url = BASE_URL + '/profiles'
        params = {'search':name}
        response = requests.get(url,params=params,headers=HEADERS)
        return response.json()

    @classmethod
    def get_profile(cls,uuid):
        url = BASE_URL + '/profiles/'+uuid
        response = requests.get(url,headers=HEADERS)
        return response.json()
    @classmethod
    def update_profile(cls,uuid,tag):
        url = BASE_URL + '/profiles/' + uuid
        data = {'tags':[tag]}
        response = requests.patch(url,json=data,headers=HEADERS)
        return response.json()

    @classmethod
    def create_tag(cls,name_tag):
        url = BASE_URL + '/tags'
        data = {'name':name_tag}
        response = requests.post(url,json=data,headers=HEADERS)
        return response.json()

    @classmethod
    def get_tags(cls):
        url = BASE_URL + '/tags'
        response = requests.get(url, headers=HEADERS)
        return response.json()

    @classmethod
    def get_proxy(cls,name):
        url = BASE_URL + '/proxies'
        response = requests.get(url, headers=HEADERS)
        proxies = response.json()['data']
        for proxy in proxies:
            if proxy['title'] == name:
                return proxy['uuid']


