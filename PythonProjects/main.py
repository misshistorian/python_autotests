import requests

URL = "https://api.pokemonbattle.ru/v2"
Token = "f33ebf5f17250a58a68da361c475f4f0"
Header = {
    "Content-Type": "application/json",
    "trainer_token": Token
}

Body_create_a_pokemon = {
    "name": "John",
    "photo_id": 12
}
'''response = requests.post(
    url=f"{URL}/pokemons",
    headers=Header,
    json=Body_create_a_pokemon
)
print(response.status_code)
print(response.text)'''



Body_change_a_pokemon = {
    "pokemon_id": "351904",
    "name": "Bun",
    "photo_id": 12
}
'''
response = requests.put(
    url=f"{URL}/pokemons",
    headers=Header,
    json=Body_change_a_pokemon
)
print(response.status_code)
print(response.text)'''



Body_add_pokemon_in_pokeball ={
    "pokemon_id": "351904"
}

response = requests.post (
    url=f"{URL}/trainers/add_pokeball",
    headers=Header,
    json=Body_add_pokemon_in_pokeball)

print(response.status_code)
print(response.text)