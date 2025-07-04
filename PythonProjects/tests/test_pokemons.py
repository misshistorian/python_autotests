import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"
Token = "f33ebf5f17250a58a68da361c475f4f0"
Header = {
    "Content-Type": "application/json",
    "trainer_token": Token
}
Trainer_id = '36044'

'''def test_sataus_code():
 response = requests.get(url = f'{URL}/trainers')
 assert response.status_code == 200'''

def test_part_of_response():
  response_get = requests.get(url = f'{URL}/trainers', params = {"trainer_id" : Trainer_id})
  

  print(response_get.json())