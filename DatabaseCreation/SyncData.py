# Get Data from Google Sheet
import sqlite3

import gspread
from google.oauth2.service_account import Credentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
]

credentials = Credentials.from_service_account_file(
    '../campaign-318908-b7f2f5f17cab.json',
    scopes=scopes
)


def return_not_matches(a, b):
    return [[x for x in a if x not in b], [x for x in b if x not in a]]


def profile_data_import(google_sheet_file_name, sheet_name, profile_life_circle ):
    gc = gspread.authorize(credentials)

    fb_username_url_gs = gc.open(google_sheet_file_name).worksheet(sheet_name)

    google_sheet_row_data = fb_username_url_gs.col_values(1)
    existingRow = len(google_sheet_row_data)

    connection = sqlite3.connect('../miracle.db')
    cursor = connection.cursor()

    databaseList = []
    databaseLists = cursor.execute("SELECT profile_link FROM facebook_profile WHERE _fk_profile_life_circle=5")
    for data in databaseLists:
        databaseList.append(data[0])
    connection.commit()
    connection.close()

    have_to_written_double_list = return_not_matches(google_sheet_row_data, databaseList)
    have_to_written = have_to_written_double_list[0]

    profile_list_index = []
    for profile_list in have_to_written:
        profile_list_index.append(profile_list)

    if len(databaseList) > len(google_sheet_row_data):
        for profile_list in profile_list_index:
            fb_username_url_gs.update_cell(existingRow + 1, 1, profile_list)

    elif len(databaseList) == len(google_sheet_row_data):
        print("Both List is up to date Sync in not needed")

    elif len(databaseList) < len(google_sheet_row_data):
        for profile_list in profile_list_index:
            print(profile_list)
            connection = sqlite3.connect('../miracle.db')
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO facebook_profile VALUES (:_pk_facebook_profile, :profile_link, :_fk_profile_name,  :_fk_profile_gender,:_fk_profile_country, :_fk_profile_life_circle)",
                {
                    '_pk_facebook_profile': None,
                    'profile_link': profile_list,
                    '_fk_profile_name': None,
                    '_fk_profile_country': None,
                    '_fk_profile_gender': None,
                    '_fk_profile_life_circle': profile_life_circle
                })
            connection.commit()
            connection.close()

    else:
        print("I have to write new logic")


# Import first_Massage_to_Python_learner
profile_data_import('Campeign 001', 'FirstMessagePythonLearner', 4)
print("Get facebook_profile from Google Sheet successfully")

# Import before_conversaton_1
profile_data_import('Campeign 001', 'before_conversation_1', 13)
print("Get facebook_profile from Google Sheet successfully")

# Import blockID
profile_data_import('Campeign 001', 'blockID', 5)
print("Get facebook_profile from Google Sheet successfully")

# Import testID
profile_data_import('Campeign 001', 'testID', 24)
print("Get facebook_profile from Google Sheet successfully")

# Import 92.deep_communication_1st
profile_data_import('Campeign 001', '92.deep_communication_1st', 23)
print("Get facebook_profile 92.deep_communication_1st data from Google Sheet successfully")

# Import 93.deep_communication_2nd
profile_data_import('Campeign 001', '93.deep_communication_2nd', 22)
print("Get facebook_profile 93.deep_communication_2nd data from Google Sheet successfully")

# Import 94.deep_communication_3rd
profile_data_import('Campeign 001', '94.deep_communication_3rd', 21)
print("Get facebook_profile 94.deep_communication_3rd data from Google Sheet successfully")

# Import 95.deep_communication_4th
profile_data_import('Campeign 001', '95.deep_communication_4th', 20)
print("Get facebook_profile 95.deep_communication_4th data from Google Sheet successfully")

# Import 96.deep_communication_5th
profile_data_import('Campeign 001', '96.deep_communication_5th', 19)
print("Get facebook_profile 96.deep_communication_5th data from Google Sheet successfully")

# Import 97.deep_communication_6th
profile_data_import('Campeign 001', '97.deep_communication_6th', 18)
print("Get facebook_profile 97.deep_communication_6th data from Google Sheet successfully")

# Import 98.deep_communication_7th
profile_data_import('Campeign 001', '98.deep_communication_7th', 17)
print("Get facebook_profile 98.deep_communication_7th data from Google Sheet successfully")

# Import 99.deep_communication_8th
profile_data_import('Campeign 001', '99.deep_communication_8th', 16)
print("Get facebook_profile 99.deep_communication_8th data from Google Sheet successfully")

# Import Profile Data
profile_data_import('Campeign 001', 'InternationPeople', 7)
print("Get facebook_profile from Google Sheet successfully")