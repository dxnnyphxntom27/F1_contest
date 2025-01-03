import requests
import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def get_race_results(season, round_number):
    url = f"http://ergast.com/api/f1/{season}/{round_number}/results.json?limit=10"
    response = requests.get(url)
    data = response.json()
    return data

def store_driver_names(race_data):
    driver_positions = {}

    for result in race_data['MRData']['RaceTable']['Races'][0]['Results']:
        position = result['position']
        print(f"Position {position}: ", end="")
        driver_id = input().strip().upper()
        driver_positions[driver_id] = int(position)

    with open('race_predictions.json', 'w') as outfile:
        json.dump(driver_positions, outfile)

race_data = get_race_results('current', 23)

drivers_dict = {
    "max_verstappen": "VER",
    "perez": "PER",
    "leclerc": "LEC",
    "piastri": "PIA",
    "alonso": "ALO",
    "russell": "RUS",
    "bearman": "BEA",
    "norris": "NOR",
    "hamilton": "HAM",
    "hulkenberg": "HUL",
    "albon": "ALB",
    "kevin_magnussen": "MAG",
    "ocon": "OCO",
    "tsunoda": "TSU",
    "sargeant": "SAR",
    "ricciardo": "RIC",
    "bottas": "BOT",
    "zhou": "ZHO",
    "stroll": "STR",
    "gasly": "GAS",
    "sainz": "SAI",
    "colapinto": "COL",
    "lawson": "LAW"
}

drivers_dict_swapped = {
    "VER": "max_verstappen",
    "PER": "perez",
    "LEC": "leclerc",
    "PIA": "piastri",
    "ALO": "alonso",
    "RUS": "russell",
    "BEA": "bearman",
    "NOR": "norris",
    "HAM": "hamilton",
    "HUL": "hulkenberg",
    "ALB": "albon",
    "MAG": "kevin_magnussen",
    "OCO": "ocon",
    "TSU": "tsunoda",
    "SAR": "sargeant",
    "RIC": "ricciardo",
    "BOT": "bottas",
    "ZHO": "zhou",
    "STR": "stroll",
    "GAS": "gasly",
    "SAI": "sainz",
    "COL": "colapinto",
    "LAW": "lawson"
}

diff_arr = [10, 8, 6, 4, 2]
driver_positions = []

for result in race_data['MRData']['RaceTable']['Races'][0]['Results']:
    driver_name = result['Driver']['driverId']
    driver_id = drivers_dict[driver_name]
    position = result['position']
    driver_positions.append({"Driver name": driver_id, "Position": position})

with open('actual_driver_positions.json', 'w') as outfile:
    json.dump(driver_positions, outfile)

print(f"Enter positions for {race_data['MRData']['RaceTable']['Races'][0]['raceName']}: \n", end="")
store_driver_names(race_data)

actual_driver_positions = load_json('actual_driver_positions.json')
race_predictions = load_json('race_predictions.json')

suma = 0
difference = 10
prediction_array = []

print(f"\nYour results for {race_data['MRData']['RaceTable']['Races'][0]['raceName']}")

for driver_pred in race_predictions:
    actual_position = None
    found = False
    difference = None

    for driver_act in actual_driver_positions:
        if driver_pred == driver_act['Driver name']:
            found = True
            actual_position = driver_act['Position']
            break

    if found:
        print(f"{driver_pred} {race_predictions[driver_pred]} [{actual_position}]")
        if race_predictions[driver_pred] <= 10:
            difference = abs(race_predictions[driver_pred] - int(actual_position))
            print("Różnica:", difference)
            if difference < 5:
                suma += diff_arr[difference]
                print(diff_arr[difference])
                prediction_array.append(diff_arr[difference])
            else:
                prediction_array.append(0)
        else:
            prediction_array.append(0)
    else:
        actual_position = "11+"
        print(f"{driver_pred} {race_predictions[driver_pred]} [{actual_position}]")
        prediction_array.append(0)

    print("-------------")

print("-------------------")
print("Suma: ", suma)
print("\n".join(map(str, prediction_array)))

