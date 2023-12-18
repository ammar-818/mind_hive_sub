import re
import json
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

"""
NOTE
- Scraping coordinates scripts from the location
extracted from website.
"""


def process_place(name_text: str):
    text = name_text.replace("ZUS", "").replace("Coffee", "")
    text = text.replace(" ", "+").strip()
    return text


def remove_non_alphanumeric(input_string):
    pattern = re.compile(r"[^a-zA-Z0-9\s]")
    result_string = pattern.sub(" ", input_string)

    return result_string


def find_coordinate(data):
    branch_names = [x["branch_name"] for x in data]
    # results = {"location": [], "lattitude": [], "longitude": []}
    results = []
    for place in tqdm(branch_names):
        data = {}
        service = Service("C:\chromedriver120\chromedriver")
        option = webdriver.ChromeOptions()

        place_upg = remove_non_alphanumeric(place)
        place_upg = process_place(place_upg)

        URL = f"https://nominatim.openstreetmap.org/ui/search.html?q={place_upg}"
        driver = webdriver.Chrome(service=service, options=option)
        driver.get(URL)
        driver.maximize_window()
        driver.implicitly_wait(2)
        try:
            button = driver.find_element("xpath", '//*[@id="searchresults"]/div[1]/a')
            button.click()
            driver.implicitly_wait(2)
            latlong = driver.find_element(
                "xpath", '//*[@id="locationdetails"]/tbody/tr[8]/td[2]'
            ).text.split(",")
            data["location"] = place
            data["lattitude"] = latlong[0]
            data["longitude"] = latlong[1]
            results.append(data)

            driver.quit()
        except:
            driver.quit()
            print(f"ERROR: {place} is not found in Open Street")
            pass

    return results


if __name__ == "__main__":
    with open("./data/zus_data.json", "r") as f:
        data = json.load(f)
    results = find_coordinate(data)
    print(results)

    with open("zus_geolocation.json", "w") as f:
        json.dump(results, f)
