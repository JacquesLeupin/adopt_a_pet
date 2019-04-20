from flask import Flask
from secret import API_SECRET_KEY
import requests
import random 

# GET https://api.petfinder.com/v2/animals


def show_response():
  """ Creates a dictionary with name, species and age of a random pet from the API """

  response = requests.get("https://api.petfinder.com/v2/animals", params={"limit" : 1, "sort": "random"}, headers={'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImZkMWMyNzU5NzZiNzczYTJiMWU5Njk5ZmI4NTJhZGZmNGQ1OGM3ZjQ1NTViOWM1ZDExYWJiMDlhYWU3ODBiNzg5ZTllNWExZTNhYmU1MjE1In0.eyJhdWQiOiJYYXF3UWpvZjJKd0dWMlI4MEpZMVcxZUxIZkVlR2FPMXQ4UVhxVjBWV01LWThWeDBPVSIsImp0aSI6ImZkMWMyNzU5NzZiNzczYTJiMWU5Njk5ZmI4NTJhZGZmNGQ1OGM3ZjQ1NTViOWM1ZDExYWJiMDlhYWU3ODBiNzg5ZTllNWExZTNhYmU1MjE1IiwiaWF0IjoxNTU1NzE3Mjc2LCJuYmYiOjE1NTU3MTcyNzYsImV4cCI6MTU1NTcyMDg3Niwic3ViIjoiIiwic2NvcGVzIjpbXX0.AiBrr2grqagMhoc5xLW6BBVvcvjagRGqEsUOrLpYJJjeFDQWYjDGIp3_CFJRSICMaBgeT13Z6GZYdawPONtasSYFJf-ZcR99SnUh9lKR-BcPOhZBFX7iK0qD7L_yZOqkHtUwQBZ9GMPSbVuC2ZB0ADh7IS4ejz3ZcyQ-uZ0WXkiLn8YBtGx5hAo2N5XuGLnpoFkgjFUYKxHvk_qzimt8YiaPhvz8Xd9xyaXhe9I7kv4UnVMmUpvgbCFuXWtZyLwnxJAibjU6eI5tK2rpkXqH90VFSmjc2JCouhsIjkLzR4A3jL6EUKsOqrDTyWH4EeZnf-7bAy18YQSDf2gN1AhwKQ"})
  response_dict = response.json() # json returns it as dictionary

  first_animal = response_dict['animals'][0] # grabs first animal

  # Grab all the stuff we need, you should use INSOMNIA next time OK KRISTINA? ok
  name = first_animal['name']
  species = first_animal['species']
  gender = first_animal['gender']
  age = first_animal['age']

  # We return a dictionary so we can do the cool python trick with ** 
  return { 
    "name" : name,
    "species" : species,
    "age" : 10 # we set to 10 becausea the stupid API does "Young, Baby, and Adult" WTF is that? so we have to use a number so the SQL requirements doesnt break
  } 


