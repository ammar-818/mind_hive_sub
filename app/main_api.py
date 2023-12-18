from fastapi import FastAPI, HTTPException, status
from utils import read_json, get_distance, get_geoloc_data

app = FastAPI(title="Mind Hive Geolocation API")

# Activate venv on Windows powershell
# $ venv/Scripts/Activate.ps1


@app.get("/")
async def get_root():
    return {"author": "Ammar Azman", "status": "ok"}


@app.get("/location", status_code=status.HTTP_200_OK)
async def get_geolocation(branch_name: str):
    data = read_json("./data/zus_geolocation.json")
    for item in data:
        if branch_name in item.values():
            return {"latitude": item["lattitude"], "longitude": item["longitude"]}
        else:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                detail=f"ERROR: {branch_name} does not exist.",
            )


@app.get("/distance", status_code=status.HTTP_200_OK)
async def get_location(point_1: str, point_2: str):
    lat_1, lat_2, lon_1, lon_2 = get_geoloc_data(point_1, point_2)
    distance = round(get_distance(lat_1, lon_1, lat_2, lon_2), 2)

    intercept = True if distance < 5 else False
    return {
        "point_1": point_1,
        "point_2": point_2,
        "distance_km": distance,
        "intercept": intercept,
    }
