from datetime import datetime, timedelta
import requests
import os
import time
import json
import pandas as pd

print("\033[33m=========ZHEN SCRIPT========\033[0m     \033[31mby jakoh, bshamsid\033[0m")
print("\033[33mTo run this script you must first insert your UID & your SECRET key below \033[0m")
print("\033[33mYou can find your secret at \033[4;33mhttps://profile.intra.42.fr/oauth/applications\033[0;33m under 'YOUR APPLICATION'\033[0m")
# SECRETS TO VALHALLA
UID = input("\033[0;35mUID: \033[0m")
SECRET = input("\033[0;35mSECRET: \033[0m")

# RESQUESTING ACCESS_TOKEN TO VALHALLA USING SECRETS
headers = {'Content-type':'application/json'}
r = requests.post(f"https://api.intra.42.fr/oauth/token?grant_type=client_credentials&client_id={UID}&client_secret={SECRET}", headers=headers)
access_token = r.json()['access_token']

# Gets all users that are linked to 42KL Campus
# 42KL Campus id number is '34' if you wish to change to your campus please change this number in 'url'
# Each call on api gives us a list of 100 users
# To get the next 100 users we change the page number
# The loop will loop till theres less than 100 users in a page
# That means we have reach the end.
def get_all_users():
    print("\033[0;33mREQUESTING FOR ALL USERS\033[0m")
    # 'i' represent the page
    # 'tol' represents the number of results in a page 100 by default
    # 'full_list' stores all the results of the users in a json array.
    i = 1
    tol = 100
    full_list = []
    while tol == 100:
        url = f"https://api.intra.42.fr/v2/campus/34/users?per_page=100&page={i}&access_token={access_token}"
        response = requests.get(url)
        full_list += response.json()
        tol = len(response.json())
        i += 1
    # output results to "user_42kl.json"
    with open("user_42kl.json","w") as f:
        f.write(json.dumps(full_list))
    print("\033[0;33mREQUEST COMPLETED\033[0m")

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

# Seperating all Users into 2 groups, one for those that are 'Cadets' into 'cadets.json'
# Another into those that are not cadets 'dumpster.json'
# We will only be using 'cadets.json' in future since thats the data that we want.
def filter_cadets():
    print("\033[0;33mFILTERING CADETS FROM PISCINERS\033[0m")
    # if .json folder already exist then use back existing ones. this is when users decide to only update the list
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
    # we loop through each user to look for those that are cadets or not
    # if user pass the cadet check then we get api call for for that specific user for more info
    # The way we check if a user is a cadet or not is by checking the number of objects in ["cursus_users"]
    # The other thing we check for is if a user is a 'Member' which is a cadet that has pass the core program
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
            print(user['login'], "discovered before")
    # After we have seperated which user is a cadet and which is not
    # Write them out to 'cadets.json' & 'dumpster.json'
    with open("cadets.json", "w") as f:
        f.write(json.dumps(passed_users))
    with open("dumpster.json", "w") as f:
        f.write(json.dumps(non_passed_users))
    print("\033[0;33mCADETS FILTERED\033[0m")

# Now that we have all of the cadets data that we need
# We loop through all the cadets to get the info that we need
# name = name of cadet, period_from = Cadets start date, level = Cadet level,
# status = 'DROPPED OUT', 'CORE PROG', 'SPECIALISATION', blackhole = Date of cadet being absorbed by blackhole
def generate_sheet():
    print(f"\033[0;33mGENERATING EXCEL SHEET\033[0m")
    with open("cadets.json", "r") as f:
        cadets = json.loads(f.read())
    data = []
    current_time = datetime.now()
    for cadet in cadets:
        user = {}
        user["name"] = cadet["cursus_users"][1]["user"]["usual_full_name"].upper()
        user["period_from"] =  datetime.strptime(cadet["cursus_users"][1]["begin_at"], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%d/%m/%Y")
        user["status"] = ""
        user["level"] = int(cadet["cursus_users"][1]["level"])
        if cadet['cursus_users'][1]['grade'] == "Member":
            user["blackhole"] = current_time
        else:
            user["blackhole"] = datetime.strptime(cadet["cursus_users"][1]["blackholed_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
        if (user["blackhole"] < current_time and cadet['cursus_users'][1]['grade'] != "Member"):
            user["blackhole"] = user["blackhole"].strftime("%d/%m/%Y")
            user["status"] = "DROPPED OUT"
        elif cadet['cursus_users'][1]['grade'] == "Member":
            user["blackhole"] = ""
            user["status"] = "SPECIALISATION"
        else:
            user["blackhole"] = ""
            user["status"] = "CORE PROG"
        data.append(user)
    df = pd.DataFrame.from_dict(data)
    df["period_from"] = pd.to_datetime(df["period_from"], format="%d/%m/%Y")
    df.sort_values(by=['period_from','name'], inplace=True)
    df["period_from"] = df["period_from"].dt.strftime('%d/%m/%Y')
    file_name = input("\033[0;35mName Your Excel File: \033[0m")
    df.to_excel(f"{file_name}.xlsx", index=False)
    print(f"\033[0;34m{file_name}.xlsx has been generated.\033[0m")
    print("\033[0;34mExit the program and type 'open .' to view the folder and get the excel\033[0m")
    print(f"\033[0;32mK Bye.\033[0m")

# This is when the program is ran
print("\033[33m=========DHARMA GENERATOR========\033[0m     \033[31mby jakoh, bshamsid\033[0m")
print("\u001b[33mTo exit program type: 'exit'\033[0m")
print("\u001b[33mTo generate full list with updated users : 'full'\033[0m")
print("\u001b[33mTo update current list: 'update'\033[0m")
ipt = input("\033[0;35mCommand: \033[0m")
while ipt != "exit":
    if ipt == "full":
        get_all_users()
        filter_cadets()
        generate_sheet()
    elif ipt == "update":
        filter_cadets()
        generate_sheet()
    print("\u001b[33mTo exit program type: 'exit'\033[0m")
    print("\u001b[33mTo generate full list with updated users : 'full'\033[0m")
    print("\u001b[33mTo update current list: 'update'\033[0m")
    ipt = input("\033[0;35mCommand: \033[0m")


