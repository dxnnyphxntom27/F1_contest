import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def store_driver_names():
    driver_positions = {}
    print("Enter your predictions for driver positions:")

    for i in range(1, 11):
        print(f"Position {i}: ", end="")
        driver_id = input().strip().upper()
        driver_positions[driver_id] = i

    with open('race_predictions.json', 'w') as outfile:
        json.dump(driver_positions, outfile)

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
    "doohan": "DOO",
    "hadjar": "HAD",
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
    "lawson": "LAW",
    "antonelli": "ANT",
    "bortoleto": "BOR",
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
    "LAW": "lawson",
    "DOO": "doohan",
    "HAD": "hadjar",
    "ANT": "antonelli",
    "BOR": "bortoleto",
}

diff_arr = [10, 8, 6, 4, 2]

# Load manually entered actual driver positions
actual_driver_positions = load_json('actual_driver_positions.json')

# Prompt user to enter predictions
store_driver_names()

# Load user predictions
race_predictions = load_json('race_predictions.json')

suma = 0
prediction_array = []

print("\nYour results:")

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
            print("Difference:", difference)
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
print("Total Score: ", suma)
print("\n".join(map(str, prediction_array)))

