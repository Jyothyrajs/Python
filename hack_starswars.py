
#No of films of an actor
#Take the character as a number and find no of films he/she acted
from urllib.request import urlopen
import json
import re
class Solution:
    def run(self, character):
        url = "https://challenges.hackajob.co/swapi/api/films/"
        response = urlopen(url)
        json_data = json.loads(response.read())
        characters = json_data["results"][0]["characters"]
        #print(result)
        for chara_url in characters:
            chara_response = urlopen(chara_url)
            chara_data = json.loads(chara_response.read())
            character_name = chara_data["name"]
            titles = []
            for film in chara_data["films"]:
                film_response = urlopen(film)
                films_detail = json.loads(film_response.read())
                titles.append(films_detail["title"])
            print(character_name)
            for films in titles:
                print(films)
            print()
            



sol = Solution()
films = sol.run("1")
#print("No of films actedi: "+str(films))
