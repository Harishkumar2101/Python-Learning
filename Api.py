import requests

# Lets Get Pokemon Data Using API

base_url = "https://pokeapi.co/api/v2"

pokemon_name = "ditto"


def get_info(name):
    print("Getting Pokemon Data")
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code==200:
        print("Pokemon Data Retrieved Succesfully ")
        Data=response.json()
        return Data
    else: 
        print("Failed To Retrieve Data")


    


My_Pokemon=get_info(pokemon_name)
if My_Pokemon:
    print(f"Name Is : {My_Pokemon['name']}")
    print(f"Weight Is : {My_Pokemon['weight']}")
    
    




