import requests
import json

#GET
user_input = input("enter id: ")
get_url = f"https://jsonplaceholder.typicode.com/todos/{user_input}"
get_response = requests.get(get_url)
print(get_response.json())

#POST
to_do_item = {'userId': 1, 'title': 'my to do', 'completed': False}
post_url = "https://jsonplaceholder.typicode.com/todos"
#optional header
headers = {"Content-Type": "application/json"}
#post_response = requests.post(post_url, json =to_do_item, headers= headers)
#print(json.dumps(to_do_item))
post_response = requests.post(post_url, data =json.dumps(to_do_item), headers= headers)
print(post_response.json())


#PUT
to_do_item_15 = {'userId': 2, 'title': 'my to do put title', 'completed': False}
put_response = requests.put(get_url, json=to_do_item_15)
print(put_response.json())


#PATCH
to_do_item_patch_15 = {"title": "patch test"}
patch_response = requests.patch(get_url, json = to_do_item_patch_15)
print(patch_response.json())

#DELETE
delete_response = requests.delete(get_url)
print(delete_response.json())
print(delete_response.status_code)
