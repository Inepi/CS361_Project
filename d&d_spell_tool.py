import asyncio
import aiohttp
import requests
import json

async def spell_search(user_input):
    spell_url = "https://www.dnd5eapi.co/api/spells/{}"

    async with aiohttp.ClientSession() as session:
        async with session.get(spell_url.format(user_input)) as resp:
            spell_response = await resp.json()
    
    #if spell_response.status == 200:
        #pass
    #elif spell_response.status == 404:
        #return print("Sorry, your requested spell wasnt found!")
    
    spell_display(spell_response)
    return

def spell_display(spell):
    print(f"{spell['name']} is a spell that allows you to do the following: ")
    print(f"{spell['desc'][0]}")
    print(f"It has a range of {spell['range']}, a casting time of {spell['casting_time']}, and is a level {spell['level']} spell.")



def spell_name_cleanup(spell_name):
    spell_name = spell_name.lower()
    spell_name = spell_name.replace(" ", "-")
    print(spell_name)
    return spell_name

user_spell_search = input("What spell are you looking for? ")
user_spell_search = spell_name_cleanup(user_spell_search)
searched_spell = asyncio.run(spell_search(user_spell_search))

                                     





