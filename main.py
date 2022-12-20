from datetime import datetime, timedelta
import requests
import os
import time
import json
import pandas as pd

UID="u-INSERT_HERE"
SECRET="s-INSERT_HERE"


headers = {'Content-type':'application/json'}
r = requests.post(f"https://api.intra.42.fr/oauth/token?grant_type=client_credentials&client_id={UID}&client_secret={SECRET}", headers=headers)
access_token = r.json()['access_token']




def get_all_users():
    print("REQUESTING FOR ALL USERS")
    i = 1
    tol = 100
    full_list = []
    while tol == 100:
        url = f"https://api.intra.42.fr/v2/campus/34/users?per_page=100&page={i}&access_token={access_token}"
        response = requests.get(url)
        full_list += response.json()
        tol = len(response.json())
        i += 1

    with open("user_42kl.json","w") as f:
        f.write(json.dumps(full_list))
    print("REQUEST COMPLETED")

def get_keys_by_type(dictionaries, key):
    # Initialize an empty list to store the keys
    keys = []

    # Iterate over the dictionaries
    for dictionary in dictionaries:
        # Iterate over the keys in the dictionary
        if key in dictionary.keys():
            keys.append(dictionary[key])

    # Return the list of keys
    return keys

def filter_cadets():
    print("FILTERING CADETS FROM PISCINERS")
    try:
        with open("user_42kl.json", "r") as f:
            users_42kl = json.loads(f.read())

        with open("cadets.json", "r") as f:
            passed_users = json.loads(f.read())

        with open("dumpster.json", "r") as f:
            non_passed_users = json.loads(f.read())
    except:
        with open("user_42kl.json", "r") as f:
            users_42kl = json.loads(f.read())
            passed_users = []
            non_passed_users = []

    passed_user_logins = get_keys_by_type(passed_users, "login")
    non_passed_user_logins = get_keys_by_type(non_passed_users, "login")
    for user in users_42kl:
        if (user['login'] not in non_passed_user_logins and user['login'] not in passed_user_logins):
            response = requests.get(f'https://api.intra.42.fr/v2/users/{user["login"]}?access_token={access_token}')
            try:
                if len(response.json()['cursus_users']) > 1 and response.json()['cursus_users'][1]['grade'] in ["Member","Learner"]:
                    passed_users.append(response.json())
                    print(f"{response.json()['login']} passed the piscine")
                else:
                    non_passed_users.append(response.json())
                    print(f"{response.json()['login']} did not pass the piscine")
            except Exception as err:
                print(f"Error occured: {err}")
        else:
            print(user['login'], "in dumpster or cadets")

    with open("cadets.json", "w") as f:
        f.write(json.dumps(passed_users))

    with open("dumpster.json", "w") as f:
        f.write(json.dumps(non_passed_users))
    print("CADETS FILTERED")

def generate_sheet():
    print(f"GENERATING EXCEL SHEET")
    with open("cadets.json", "r") as f:
        cadets = json.loads(f.read())
    data = []
    current_time = datetime.now()
    for cadet in cadets:
        user = {}
        user["name"] = cadet["cursus_users"][1]["user"]["usual_full_name"]
        user["preiod_from"] =  datetime.strptime(cadet["cursus_users"][1]["begin_at"], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%d-%b-%Y")
        if cadet['cursus_users'][1]['grade'] == "Member":
            user["blackhole"] = current_time
        else:
            user["blackhole"] = datetime.strptime(cadet["cursus_users"][1]["blackholed_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
        user["level"] = int(cadet["cursus_users"][1]["level"])
        if (user["blackhole"] < current_time and cadet['cursus_users'][1]['grade'] != "Member"):
            user["blackhole"] = user["blackhole"].strftime("%d-%b-%Y")
            user["status"] = "DROPPED OUT"
        elif cadet['cursus_users'][1]['grade'] == "Member":
            user["blackhole"] = ""
            user["status"] = "SPECIALISATION"
        else:
            user["blackhole"] = ""
            user["status"] = "CORE PROG"
        data.append(user)
    df = pd.DataFrame.from_dict(data)
    df.to_excel(f"{current_time}.xlsx", index=False)
    print(f"K Bye.")

print("=========ZHEN SCRIPT========")
print("To exit program type : 'exit'")
print("To generate full list with updated users : 'full'")
print("To update current list: 'update'")
ipt = input("Command: ")
while ipt != "exit":
    if ipt == "full":
        get_all_users()
        filter_cadets()
        generate_sheet()
    elif ipt == "update":
        filter_cadets()
        generate_sheet()
    ipt = input("Command: ")

# get_all_users()
# filter_cadets()
# generate_sheet()
