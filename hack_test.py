
#No of films of an actor
#Take the character as a number and find no of films he/she acted
from urllib.request import urlopen
import json
import re
class Solution:
    def run(self, film):
        url = "https://challenges.hackajob.co/swapi/api/films/"
        response = urlopen(url)
        json_data = json.loads(response.read())
        films = json_data["results"]
        film_chars = []
        for film in range(len(films)):
            print(json_data["results"][film]["title"])
            if(json_data["results"][film]["title"] == film):
                for chara_url in json_data["results"][film]["characters"]:
                    chara_response = urlopen(chara_url)
                    chara_data = json.loads(chara_response.read())
                    character_name = chara_data["name"]
                    film_chars.append(character_name)

        for chars in film_chars:
            print(chars)
        #for chara_url in characters:
            #chara_response = urlopen(chara_url)
            #chara_data = json.loads(chara_response.read())
            #character_name = chara_data["name"]
            #titles = []
            #for film in chara_data["films"]:
                #film_response = urlopen(film)
                #films_detail = json.loads(film_response.read())
                #titles.append(films_detail["title"])
            #print(character_name)
            #for films in titles:
                #print(films)
            #print()
            



sol = Solution()
films = sol.run("A New Hope")
#print("No of films actedi: "+str(films))
