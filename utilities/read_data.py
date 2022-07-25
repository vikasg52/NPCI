import csv
import json
import os.path
import random
import re

# ==============================================================================
USER_ID_FILE_PATH = os.path.abspath('data/users.csv')


def listToString(s):
    """convert a list to string"""
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


# lOGIN api data
def get_login_data():
    """Returns a json string with the changed values required for importing orders"""
    data = {}

    # Get Json template
    with open(USER_ID_FILE_PATH) as jsonFile:
        data = json.load(jsonFile)

    return json.dumps(data)


def read_csv_file2(filepath):
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def read_csv_file(filepath):
    with open(filepath) as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                # print(f'\t{row[0]} username {row[1]} password')
                user_id = list(str({row[0]}) + ",")
                user_id = row
                # print(user_credentials)
                line_count += 1
        # print(f'Processed {line_count} lines.')
        print(user_id)
        return user_id


def get_user():
    """Returns users credentials"""
    print("USER_ID_FILE_PATH" * 5)
    print(USER_ID_FILE_PATH)
    chosen_row = ''
    path = USER_ID_FILE_PATH
    if os.path.exists(path):
        with open(path) as f:
            reader = csv.reader(f)
            for index, row in enumerate(reader):
                if index == 0 or index == 1:
                    chosen_row = row
                else:
                    r = random.randint(1, index)
                    if r == 1:
                        chosen_row = row
    print("chosen_row" * 5)
    print(chosen_row)
    return str(chosen_row)


def get_user_id():
    """Returns a json string with the changed values required for importing orders"""
    user_credentials = str(get_user())
    print("********" * 10)
    print(user_credentials)
    print(user_credentials[0])
    data = {"user_id": user_credentials[0]}
    print("********" * 10)
    # print(json.dumps(data))
    return json.dumps(data)
