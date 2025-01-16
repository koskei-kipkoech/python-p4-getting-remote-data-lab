import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f'Requests failed with statusode {response.status_code}')

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)