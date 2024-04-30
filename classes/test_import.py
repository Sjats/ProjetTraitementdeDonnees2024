import json
from pprint import pprint

with open('/Users/Sunifred/Documents/GitHub/ProjetTraitementdeDonnees2024/classes/world_country_boundaries.geojson.json') as json_data:
    d = json.loads(json_data)
    json_data.close()
    pprint(d)