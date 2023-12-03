import re
import requests
import urllib3
urllib3.disable_warnings()

steam_api = "https://store.steampowered.com/api/appdetails?appids={}"
pattern = re.compile(r'appid_(\d+):(.+)')

steam_names = {}
with open("steam-names.txt", encoding="utf8") as file:
  data = file.read().strip()
  lines = data.split('\n')
  for line in lines:
    match = re.match(r'(\d+) (.+)', line)
    app_id, name = match.groups()
    steam_names[app_id] = name

with open("steam-descriptions.txt", encoding="utf8") as file:
  dict_descriptions = {}
  list_of_names = []
  data = file.read().strip()
  lines = data.split('\n')
  for line in lines:
      match = pattern.match(line)
      app_id, description = match.groups()

      name = steam_names[app_id]

      # req = requests.get(steam_api.format(app_id), verify=False)
      # json = req.json()
      # if not json or not json[app_id] or not json[app_id]['success']:
      #   name = f"UNKNOWN GAME, app id {app_id}"
      # else:
      #   name = json[app_id]['data']['name']
      print(app_id, name)
      str = f"-- {name} --\n{description}"
      dict_descriptions[name] = str
      list_of_names.append(name)
    
list_of_names.sort()
final_string = ""
for name in list_of_names:
  final_string += dict_descriptions[name]
  final_string += '\n\n'
unicode = final_string.encode('utf8')
print(final_string)
with open("steam-descriptions-formated.txt", "wb") as write:
  write.write(unicode)