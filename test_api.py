import pytest
from api import PetFriends
from user_data import user__email, user__password, pet, new_pet

pf = PetFriends()
api_key = None
pets_list = None

# Тесты на получение api
def test_get_api_for_valid_user(email=user__email, password=user__password):
  status, result = pf.get_api_key(email, password)
  global api_key
  api_key = result
  assert status == 200
  assert 'key' in result

def test_get_api_for_invalid_user(email="email", password="pas"):
  status = pf.get_api_key(email, password)[0]
  assert status == 403
  
# Получаение спска животных
def test_get_pets_list_for_valid_user():
  status, result = pf.get_pets_list(api_key, "my_pets")
  global pets_list
  pets_list = result
  assert status == 200
  assert 'pets' in result

def test_get_pets_list_for_invalid_user():
  fake_api_key = {"key": "ERROR"}
  status = pf.get_pets_list(fake_api_key, "my_pets")[0]
  assert status == 403

# Добавление животных
def test_post_pets_for_valid_pet():
  status = pf.post_pets(api_key, pet)[0]
  assert status == 200

def test_post_pets_for_invalid_pet():
  status = pf.post_pets(api_key, "BAD PET")[0]
  assert status == 400 or 403

# Изменение животных
def test_put_pet_for_valid_pet_id_and_data():
  status = pf.put_pet(api_key, pets_list['pets'][0]['id'], new_pet)
  assert status == 200

def test_put_pet_for_invalid_pet_id():
  status = pf.put_pet(api_key, "", new_pet)
  assert status == 404

def test_put_pet_for_invalid_pet_data():
  status = pf.put_pet(api_key, pets_list['pets'][0]['id'], {"name": "a"})
  assert status == 400 or 403

# Удаление животных
def test_del_pet_for_valid_pet_id():
  status = pf.del_pet(api_key, pets_list['pets'][0]['id'])
  assert status == 200

def test_del_pet_for_invalid_pet_id():
  status = pf.del_pet(api_key, "")
  assert status == 404