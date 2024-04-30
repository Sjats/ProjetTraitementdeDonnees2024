import geojson

with open("classes/world_country_boundaries.geojson.json") as f:
    gj = geojson.load(f)
features = gj['features'][0]

