//Identify the no of films characters identified
from urllib.request import urlopen
import json

class Solution:
        
	def run(self, film, character):
		url = "https://challenges.hackajob.co/swapi/api/films/"
		response = urlopen(url)
		json_data = json.loads(response.read())
		characters = json_data["results"][0]["characters"]
		for chara_url in characters:
			chara_response = urlopen(chara_url)
			chara_data = json.loads(chara_response.read())
			character_name = chara_data["name"]
			titles = []
			for film in chara_data["films"]:
				film_response = urlopen(film)
				films_detail = json.loads(film_response.read())
				titles.append(films_detail["title"])
				#print(character_name)
				titles.sort()
				#for films in titles:
					#print(films)
					#print()
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
					#for chars in film_chars:
					#	print(chars)
		#film_chars.sort()
		#for x in film_chars:
		#	titles.append(x)
		return titles
sol = Solution()
filmsAndCharacters = sol.run("A New Hope","Raymus Antilles")
for x in filmsAndCharacters:
    print(x)
#filmsAndCharacters = None
#filmsAndCharacters = sol.run("A New Hope","1")
#return filmsAndCharacters

