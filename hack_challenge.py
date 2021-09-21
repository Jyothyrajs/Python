
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
        result = json_data["results"][0]["characters"]
        for char_link in result:
            obj = json.dumps(char_link)
            #print(obj)
            x = re.split("/",obj)
            print(x)
            if(x[-2] == character):
                char_response = urlopen(char_link)
                break
        json_data = json.loads(char_response.read())
        result = json_data["films"]
        numberOfFilms = 0
        for film in result:
            numberOfFilms += 1

        return numberOfFilms

sol = Solution()
films = sol.run("1")
print("No of films actedi: "+str(films))
