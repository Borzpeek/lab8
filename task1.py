import requests

post_id = 1
url = f'https://jsonplaceholder.typicode.com/todos/{post_id}'
response = requests.get(url)

print("Response Content:")
print(response.json())

if response.status_code in (range(400, 500) + range(500, 600)):
    print(f"Error: {response.status_code}")

class ToDo:
    def __init__(self, userId, id, title, completed):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed

new_todo_object = ToDo(userId=1, id=post_id, title="Example Todo", completed=False)

new_todo_item = {
    "userId": new_todo_object.userId,
    "title": new_todo_object.title,
    "completed": new_todo_object.completed
}
post_response = requests.post('https://jsonplaceholder.typicode.com/todos', json=new_todo_item)

print("\nPOST Response Content:")
print(post_response.json())

if post_response.status_code in (range(400, 500) + range(500, 600)):
    print(f"Error: {post_response.status_code}")

new_todo_object.completed = True

put_url = f'https://jsonplaceholder.typicode.com/todos/{post_id}'
put_response = requests.put(put_url, json=new_todo_item)

print("\nPUT Response Content:")
print(put_response.json())

if put_response.status_code in (range(400, 500) + range(500, 600)):
    print(f"Error: {put_response.status_code}")