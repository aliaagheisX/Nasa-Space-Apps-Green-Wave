import json

def read_map_from_fetched(path, output_path):
    mapping = []

    with open(path, "r" ) as f:
        while True:
            line = f.readline()
            
            if line == '':
                break
            
            row = line.strip().split()
            mapping += [{
                "iv": int(row[0]),
                "ih": int(row[1]),
                "lon_min": float(row[2]),
                "lon_max": float(row[3]),
                "lat_min": float(row[4]),
                "lat_max": float(row[5]),
            }]

    with open(output_path, "w") as f:
        json.dump(mapping, f, indent=4)
        
    return mapping

# getting iv, ih from json
def get_map(path):
    with open(path, "r") as f:
        return json.load(f)
    return []

def from_lonlat_to_vh(lon, lat, path):
    map = get_map(path)
    
    for reading in map:
        if reading["lon_min"] < lon < reading["lon_max"] and reading["lat_min"] < lat < reading["lat_max"]:
            return reading["iv"], reading["ih"]
    return 0, 0

def get_bounding_from_vh(v, h, path):
    map = get_map(path)
    for reading in map:
        if reading["iv"] == v and reading["ih"] == h:
            return reading
    return {} 
    