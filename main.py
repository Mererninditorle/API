from api import PetFriends
from user_data import user__email, user__password, pet, new_pet


pf = PetFriends()
status, result_get_api_key = pf.get_api_key(user__email, user__password)
print(status, result_get_api_key)

status, result_get_pets_list = pf.get_pets_list(result_get_api_key, "my_pets")
print("-------------------\n", status, result_get_pets_list)

status, result_post_pets = pf.post_pets(result_get_api_key, pet)
print("-------------------\n", status, result_post_pets)

status = pf.put_pet(result_get_api_key, result_get_pets_list['pets'][0]['id'], new_pet)
print("-------------------\n", status)

status = pf.del_pet(result_get_api_key, result_get_pets_list['pets'][0]['id'])
print("-------------------\n", status)