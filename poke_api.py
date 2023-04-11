import requests
import sys


POKE_API_URL = 'https://pokeapi.co/api/v2/'

def get_pokemon(pokemon):
    
    search_string = "pokemon/" + str(pokemon).lower()

    req_url = POKE_API_URL + str(search_string)

    resp_msg = requests.get(req_url)
    
    #Verify that the response is successful.
    if resp_msg.status_code == requests.codes.ok:
        print('success')
        return resp_msg.json()
    else:
        print('failure')
        print(f'response code: {resp_msg.status_code} ({resp_msg.reason})')
        exit()

def get_pokemon_name():
    if len(sys.argv) < 3:
        return sys.argv[1] 

def construct_paste(pokemon_info):
    
    title = str(pokemon_info['name']).title() + "'s Abilitys"
    body = list()
    
    for ab in pokemon_info['abilities']:
        body.append(f"- {ab['ability']['name']}")
    
    return (title, "\n".join(body))