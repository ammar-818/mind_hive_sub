import json
import math
import numpy as np
from typing import Tuple


def read_json(jsonfile) -> list[dict]:
    with open(jsonfile, "r") as f:
        data = json.load(f)
    return data


def get_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    R = 6371  # Earth's radius in kilometers

    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Differences in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance in kilometers
    distance = R * c

    return distance


def get_geoloc_data(point_1: str, point_2: str) -> Tuple[float, float, float, float]:
    data = read_json("./data/zus_geolocation.json")

    point_1_data, point_2_data = [], []

    for item in data:
        if point_1 in item.values():
            point_1_data.append(item)
        elif point_2 in item.values():
            point_2_data.append(item)

    data_1, data_2 = point_1_data[0], point_2_data[0]

    lat_1 = np.float32(data_1["lattitude"])
    lat_2 = np.float32(data_2["lattitude"])

    lon_1 = np.float32(data_1["longitude"])
    lon_2 = np.float32(data_2["longitude"])

    return lat_1, lat_2, lon_1, lon_2


if __name__ == "__main__":
    geoloc_data = get_geoloc_data(
        "DATARAN PAHLAWAN, MELAKA", "ZUS Coffee - Sungai Udang"
    )
    print(geoloc_data)
