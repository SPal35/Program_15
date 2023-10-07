import math

def calculate_distance(lat1, lon1, lat2, lon2):
    radius = 6371.0
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c
    return distance
lat1, lon1 = 52.5200, 13.4050  
lat2, lon2 = 48.8566, 2.3522   
distance = calculate_distance(lat1, lon1, lat2, lon2)
print(f"The distance between the two locations is approximately {distance:.2f} kilometers.")
