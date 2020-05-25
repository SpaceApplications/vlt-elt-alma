import json
import requests


class API:
    BASE_URL = 'https://www.eso.org/copdemo/api'
    API_URL = f'{BASE_URL}/v1'

    def connect(self):
        response = requests.post(
            f'{self.BASE_URL}/login',
            data={'username': '52052', 'password': 'tutorial'})
        self.access_token = response.json()['access_token']

    def make_request(self, method, url, data=None):
        url = f'{self.API_URL}{url}'
        headers = {'Authorization': f'Bearer {self.access_token}'}
        if data:
            data = json.dumps(data)
            return requests.request(method, url, headers=headers, data=data)
        return requests.request(method, url, headers=headers)

    def create_observing_block(self):
        data = {'itemType': 'OB', 'name': 'dummy observing block'}
        response = self.make_request('POST', '/containers/1448455/items', data)
        return response.json()['obId']
