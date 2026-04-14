import random

def get_location():
    # Simulated GPS coordinates
    lat = round(random.uniform(12.0, 13.0), 6)
    lon = round(random.uniform(77.0, 78.0), 6)

    return {"latitude": lat, "longitude": lon}
