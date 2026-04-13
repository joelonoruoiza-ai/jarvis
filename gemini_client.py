import requests

class GeminiClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.google.com/gemini'

    def _headers(self):
        return {'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'}

    def get_model_info(self, model_name):
        url = f'{self.base_url}/models/{model_name}'
        response = requests.get(url, headers=self._headers())
        return response.json()

    def generate_text(self, model_name, prompt):
        url = f'{self.base_url}/generate/{model_name}'
        payload = {'prompt': prompt}
        response = requests.post(url, json=payload, headers=self._headers())
        return response.json()