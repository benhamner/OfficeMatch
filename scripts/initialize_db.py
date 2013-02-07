import json
import requests


organizations = [{"name": "Kaggle"},
                 {"name": "Moserware"},
                 {"name": "Oberon Socks"}]

sports = [{"name": "Ping Pong", "bigger_score_better": True},
          {"name": "Soccer", "bigger_score_better": True},
          {"name": "Golf", "bigger_score_better": False}]

leagues = [{"name": "Ping Pong Minors"}]

users = [{"name": "Ben", "organization_id": 1},
         {"name": "Chris", "organization_id": 1},
         {"name": "David", "organization_id": 1}]

games = [{"league_id": 1},
         {"league_id": 1}]

scores = [{"game_id": 1, "user_id": 1, "score": 16},
          {"game_id": 1, "user_id": 2, "score": 21},
          {"game_id": 1, "user_id": 1, "score": 16},
          {"game_id": 1, "user_id": 3, "score": 21}]

tables = [("organizations", organizations),
          ("sports", sports),
          ("leagues", leagues),
          ("users", users),
          ("games", games),
          ("scores", scores)]

for table_name, data_list in tables:
    for data in data_list:
        r = requests.post("http://127.0.0.1:5000/api/%s" % table_name, 
                          data=json.dumps(data))

