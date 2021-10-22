# Find the number of goals of all the teams
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
        for round in range(len(data_json["rounds"])):
            for item in range(len(data_json["rounds"][round]["matches"])):
                if((data_json["rounds"][0]["matches"][item]["team1"]["key"]) == self.teamKey):
                    goals = goals + data_json["rounds"][0]["matches"][item]["score1"]
                    
                elif((data_json["rounds"][0]["matches"][item]["team2"]["key"]) == self.teamKey):
                    goals = goals + data_json["rounds"][0]["matches"][item]["score2"]
        return goals

url = "https://s3.eu-west-1.amazonaws.com/hackajob-assets1.p.hackajob/challenges/football_session/football.json"
response = urlopen(url)
data_json = json.loads(response.read())
teams = []
for round in range(len(data_json["rounds"])):
    for item in range(len(data_json["rounds"][round]["matches"])):
        team1 = ((data_json["rounds"][0]["matches"][item]["team1"]["key"]) )
        team2 = ((data_json["rounds"][0]["matches"][item]["team1"]["key"]) )
        team1_exist = 0
        team2_exist = 0
        for x in teams:
            if(x == team1):
                team1_exist = 1
            if( x == team2 ):
                team2_exist = 1
            if( team1_exist == 1 or team2_exist == 1):
                break
        if(team1_exist == 0):
            teams.append((data_json["rounds"][0]["matches"][item]["team1"]["key"]) )
        if(team2_exist == 0):
            teams.append((data_json["rounds"][0]["matches"][item]["team2"]["key"]) )
for team in teams:
    ft= Solution(team)
    g = ft.run()
    print("No of goals of ",team,":",g)
