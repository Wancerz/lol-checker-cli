from pprint import pprint
import json

from riotwatcher import LolWatcher, ApiError

lol_watcher = LolWatcher('API-key')

my_region = 'eun1'
# dr Józef Boksa
# print(match_list)
# pprint(match)
# print(match['metadata']['participants'][0])
# json_string = json.dumps(match,indent=5)

# with open('json_data.json', 'w') as outfile:
#     outfile.write(json_string)

# print(len(match['metadata']['participants']))
# print(len(match['info']['participants']))
username = input("podaj nazwe uzytkownika: ")
me = lol_watcher.summoner.by_name(my_region, username)

match_list = lol_watcher.match.matchlist_by_puuid(my_region,me['puuid'],count= 50)
# print(match_list)
# match = lol_watcher.match.by_id(my_region,match_list[0])
match_count = 0
# print(match['info']['participants'][1]['summonerName'])
for x in range (0, len(match_list)):
    match = lol_watcher.match.by_id(my_region,match_list[x])
    while match_count < 20:
        if match['info']['gameMode'] == 'ARAM': 
            match_count = match_count + 1
            for x in range (0,10):
                if match['info']['participants'][x]['summonerName'] == username:
                    kills = str(match['info']['participants'][x]['kills'])
                    deaths = str(match['info']['participants'][x]['deaths'])
                    assists = str(match['info']['participants'][x]['assists'])
                    champion_name = str(match['info']['participants'][x]['championName'])

                    if  match['info']['participants'][x]['win'] == True:
                        game_status = "WIN"
                    else:
                        game_status = "LOSE"


                    print("K/D/A: " + kills + "/" + deaths + "/" + assists + " " + champion_name + " " + game_status)
                    break
            break
        else:
            break
    if match_count == 20:
        break



