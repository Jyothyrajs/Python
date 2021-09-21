from urllib.request import urlopen
import json

class Solution:
    def __init__(self,name):
        self.teamKey = name

    def run(self):
        url = "https://s3.eu-west-1.amazonaws.com/hackajob-assets1.p.hackajob/challenges/football_session/football.json"
        response = urlopen(url)
        data_json = json.loads(response.read())
        goals = 0
        print(type(self.teamKey))
        for round in range(len(data_json["rounds"])):
            for item in range(len(data_json["rounds"][round]["matches"])):
            #print(type(data_json["rounds"][0]["matches"][item]["team1"]["name"]))
                if((data_json["rounds"][0]["matches"][item]["team1"]["key"]) == self.teamKey):
                    goals = goals + data_json["rounds"][0]["matches"][item]["score1"]
                #print((data_json["rounds"][0]["matches"][item]["score1"]))
                    
                elif((data_json["rounds"][0]["matches"][item]["team2"]["key"]) == self.teamKey):
                    goals = goals + data_json["rounds"][0]["matches"][item]["score2"]
                #print((data_json["rounds"][0]["matches"][item]["team2"]["name"]))
        return goals
ft= Solution("burnley")
g = ft.run()
print("No of goals : ",g)
