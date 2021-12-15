import json
import requests

class PetFriends:
  def __init__(self):
    self.base_url = "https://petfriends1.herokuapp.com/"


  def get_api_key(self, email: str, password: str) -> json:
    headers = { 'email': email, 'password': password }
    
    res = requests.get(self.base_url+'api/key', headers=headers)
    status = res.status_code
    result = ""

    try:
      result = res.json()
    except json.decoder.JSONDecodeError:
      result = res.text
    return status, result


  def get_pets_list(self, api_key, filter='') -> json:
    headers = { 'auth_key': api_key["key"] }
    filter = { 'filter': filter }

    res = requests.get(self.base_url+'api/pets', params = filter, headers=headers)
    
    status = res.status_code
    result = ""

    try:
      result = res.json()
    except json.decoder.JSONDecodeError:
      result = res.text
    return status, result

  def post_pets(self, api_key, data='') -> json:
    headers = { 'auth_key': api_key["key"] }

    res = requests.post(self.base_url+'api/create_pet_simple', headers=headers, data=data)
    
    status = res.status_code
    result = ""

    try:
      result = res.json()
    except json.decoder.JSONDecodeError:
      result = res.text
    return status, result

  def del_pet(self, api_key, pet__id = str) -> json:
    headers = { 'auth_key': api_key["key"] }

    res = requests.delete(self.base_url+f'api/pets/{pet__id}', headers=headers)
    
    status = res.status_code
    return status

  def put_pet(self, api_key, pet__id = str, data = str) -> json:
    headers = { 'auth_key': api_key["key"] }

    res = requests.put(self.base_url+f'api/pets/{pet__id}', headers=headers, data=data)
    
    status = res.status_code
    return status