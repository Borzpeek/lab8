import requests
import json
import random
from character import Character
from episode import Episode

random_character_id = random.randint(1, 826)
character_url = f'https://rickandmortyapi.com/api/character/{random_character_id}'
character_response = requests.get(character_url)

print("Character JSON Response:")
print(json.dumps(character_response.json(), indent=2))

print("\nKeys in JSON Response:")
print(character_response.json().keys())

file_name = f"info_character_{random_character_id}.json"
with open(file_name, 'w') as file:
    json.dump(character_response.json(), file, indent=2)

episode_urls = character_response.json()['episode']
episode_ids = [int(url.split('/')[-1]) for url in episode_urls]
episode_file_name = f"all_episodes_with_character_{random_character_id}.json"
with open(episode_file_name, 'a') as episode_file:
    for episode_id in episode_ids:
        episode_file.write(f"https://rickandmortyapi.com/api/episode/{episode_id}\n")

episode_response = requests.get('https://rickandmortyapi.com/api/episode/1')
print("\nEpisode JSON Response Structure:")
print(json.dumps(episode_response.json(), indent=2))

character_response_structure = requests.get('https://rickandmortyapi.com/api/character/1')
print("\nCharacter JSON Response Structure:")
print(json.dumps(character_response_structure.json(), indent=2))

episode_ids = [1, 2, 3] 

episode_objects = []

for episode_id in episode_ids:
    episode_url = f'https://rickandmortyapi.com/api/episode/{episode_id}'
    episode_response = requests.get(episode_url)
    
    if episode_response.status_code == 200:
        episode_data = episode_response.json()
        episode_object = Episode(
            episode_id=episode_data['id'],
            name=episode_data['name'],
            air_date=episode_data['air_date'],
            episode=episode_data['episode'],
            characters=episode_data['characters']
        )
        episode_objects.append(episode_object)

for episode_object in episode_objects:
    print(episode_object)
    print(f"Characters Count: {episode_object.get_characters_count()}")
    print("------")

random_character_object = Character(random_character_id)

print("Character Information:")
print(random_character_object)

random_character_object.move_to_location("Earth")

print("\nFinal Result:")
print(random_character_object.get_character_info())
