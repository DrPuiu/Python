import json
import requests
from bs4 import BeautifulSoup
import schedule
import time
import os

BASE_URL = "https://www.autovit.ro"
JSON_PATH = "./autovit_cars.json"


def crawl_autovit():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {BASE_URL}: {e}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")

    car_details = []

    #info_sections = soup.findAll('section', {'aria-label': 'Information'})
    name_sections = soup.findAll('a', {'aria-label': True})
    characteristics_sections = soup.findAll('section', {'aria-label': 'Characteristics'})
    price_sections = soup.findAll('section', {'aria-label': 'Price'})

    for item1, item2, item3 in zip(name_sections, characteristics_sections, price_sections):
        name = item1['aria-label'].split('aria-label=')[-1]

        characteristics = item2.find_all('li')
        year = characteristics[0].get_text().replace(" ", "")
        mileage = characteristics[1].get_text()
        model = characteristics[2].get_text()
        if len(characteristics) == 4:
            engine_size = characteristics[3].get_text()
        else:
            engine_size = 'N/A'

        price = item3.text.replace("EUR", " EUR")

        car_detail = {
            "name": name,
            "year": year,
            "mileage": mileage,
            "model": model,
            "engine_size": engine_size,
            "price": price
        }
        car_details.append(car_detail)

    return car_details


def write_to_json(data):
    try:
        if os.path.exists(JSON_PATH):
            with open(JSON_PATH, 'r', encoding='utf-8') as json_file:
                existing_data = json.load(json_file)

            if isinstance(existing_data, list):
                # If existing data is a list, extend it with the new data
                existing_data.extend(data)
            else:
                # If existing data is a dictionary, convert it to a list
                existing_data = [existing_data, data]
        else:
            existing_data = data

        with open(JSON_PATH, 'w', encoding='utf-8') as json_file:
            json.dump(existing_data, json_file, ensure_ascii=False, indent=2)
            json_file.write("\n")

        print(f"Data written to {JSON_PATH}")
    except Exception as e:
        print(f"Error writing to {JSON_PATH}: {e}")


def job():
    print("Crawling Autovit...")
    car_details = crawl_autovit()
    write_to_json(car_details)


def main():
    # Schedule the job to run once a day at 2:00 AM
    schedule.every().day.at("02:00").do(job)
    job()
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)


if __name__ == "__main__":
    main()
