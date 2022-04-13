from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

#google spreadsheet variables
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = {
  "type": "service_account",
  "project_id": "joy-studio-347109",
  "private_key_id": "75091a88d7a40c88a2422ef302c51accf2785fea",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDAxrZgLy/8Dd8i\nSBjjevCt4itDYhz888UooilemW0sZl2qX8NneMc1CtaCLvEk1gN7CFztTXNiBsZr\nrwwlKE1W0erTpVf1ez5fEWQXxEE3Q2iFaiUjarHXYe2whu0lX5B/iAyCmKBJgzop\n41bEC8eJzUnxKzzDmH95nC4NWb2wD/O10FaEyDm9OFEpW/YrOqGjoo5LC9N9CSVH\n6f22GBUWY2hnUeoVCFldGAUa0vAPOqco0dBpPPrZQgM64m6NlC9L3H4oxSPdos/L\nt/BISXOSgEEFtR0vDIDK7qOVGWhfL+8cKoE4mA6UaV7QFiy+xSWGz8fZ4et5Ecp4\n6F7ru4QXAgMBAAECggEACl7hu83rxv8GC1felS7bKxL9qdT8B8/siyPZA3d0h3Fy\noTtpezPkzU98KgVw5ON78byJy9PF5hIyhXXKOrATbQrDO8f9seIDpeUz+KMO1atT\nUsl/QvlJEqrTyySzo7YjekDkD2Y7AK38zR2ncsnKlOa7aqwvlHHi+kbFI79wYgUM\nBysTs38HwkcZJIVQWRmElFZD3KnGLg4ivCRQODKqLXU9UPY7BQ+NtGdt4TwrxgtM\nsGjHJ7CVogLnPBG2q2+gduzW9W7l0RV29evlJwMSTxeC2yumKx6N0fvkvXLeCqTP\nIFr4DQJEpJ7R9+a2ao9Jzp1fWxTqEDZLRERleh1JIQKBgQDpD3HVtIyyz5d2ZqmB\nOU6iYuU/7ANpxsZVb7KdD0zmI7SB3gJdAfxTbn0sRM2GdYbmthLpedZ49DLvLnbi\nLOi6yrsp6G8IqamYVukcudGC6c6XyyK7WGtOJljTcdH+vW6I0rlePF5kYWw3OAl9\nVqoa5TcmTy0Ws37pY1d49/N8YQKBgQDTwDSwVPgZhyip0+YObg9Ue491a5r788ft\nlE+vsrHYltTPNrJpf/aQHRY72DYaRzSpHVZD4SFrsIsF1EO5hTUx3AMAcuzpSM2B\nwCrwM/v6+oTNOwh0NyOpx27rOQX3CmyslpQxm4qdbC2EdnWFyTqDMBj6YnHc7mrX\nUEqKlMGTdwKBgC/4/+OPYI7F8FVs2GNDGo6OcMXxnNo/EkAv18JAjgGpQ9SfkDj4\n2amKyrU8DForAvOmcsogTCdljL5zAAGaYOViKZh8wa40zjYPXbiN/zRFUEMqiyGp\nF51kg1Ay05juATyks4dUQdHDw/Sx0jI8jpMur2VxUsSjefIsgqrhzvrBAoGBAJS+\n/wQjHAkqtbjevkvCqogpJ/RO+5cjf3z34yZD+8Ru590LyjZsCnLfy9+MGS1KecaW\nciPKwORaJr6Yhl6LIXv91in5kUyqtJoBuOf1THvYgXN9lYm1thqsmtEnxHXuX7q5\nKC7U2YGOHUdgw1uQqMbBAbrZbqzI2kqX/1Tr/DMvAoGBAOfeNHAqeSU82s79OJEv\ngef8gAq33p7dp3efBkv6RHJ/CvWD2xC+K+jE1nDTCvt8tqesX+vhNIrV5OR360LF\nrczwxy9hM2IcoTbp38pYhJeZQEXK/67kinGmC3cz0dLh2cv9qlCBaAMLaWsW/GZY\nLCPGuqIH/5eV9rpLs2ZTW/hV\n-----END PRIVATE KEY-----\n",
  "client_email": "main-master@joy-studio-347109.iam.gserviceaccount.com",
  "client_id": "102969667770255232709",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/main-master%40joy-studio-347109.iam.gserviceaccount.com"
}
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
MAIN_SPREADSHEET_ID = '1fv8FiV0rdHgEQj758zS7qFP1McsvQwuBNdLCaMxU0Vw'
INDIVIUAL_SPREADSHEET_ID = '1zPLgCz9rGbUHck7cv_fkjtIapXjj6JTNpc0YdQWD-40'

#spreadsheet functions
def read_main_spreadsheet():
    try:
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=MAIN_SPREADSHEET_ID,
                                    range="Main!A1:H10000").execute()
        values = result.get('values', [])
        return values
        
    except HttpError as err:
        return err

def read_individual_spreadsheet(username):
    try:
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=INDIVIUAL_SPREADSHEET_ID,
                                    range=f"{username}!A1:L10000").execute()
        values = result.get('values', [])
        return values
        
    except HttpError as err:
        return err


def write_main_spreadsheet(position, data):
    try:
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        request = sheet.values().update(spreadsheetId=MAIN_SPREADSHEET_ID, range=f"main!{position}1",
                                        valueInputOption="USER_ENTERED",
                                        body={"values": data}).execute()
    except HttpError as err:
        return err

def write_individual_spreadsheet(user, position_to_add, data):
    try:
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        body = { 'values' : [data, ['','','','','','','','','','','','']]}
        request = sheet.values().update(spreadsheetId=INDIVIUAL_SPREADSHEET_ID, range=f"{user}!A{position_to_add}",
                                        valueInputOption="USER_ENTERED",
                                        body=body).execute()
    except HttpError as err:
        return err


def get_worksheets():
    #get the indivudual spreadsheets with weekly data
    service = build('sheets', 'v4', credentials=creds)
    spreadsheet = service. spreadsheets().get(spreadsheetId=INDIVIUAL_SPREADSHEET_ID).execute()
    worksheets = []
    for i in range(len(spreadsheet['sheets'])):
        worksheet = spreadsheet['sheets'][i]['properties']["title"]
        worksheets.append(worksheet)
    return worksheets

def sheetProperties(title, **sheetProperties):
    default_Properties = {
        'properties' :{
            'title': title, 
            'index' : 0,
            'sheetType' : 'GRID',
            'hidden' : False
            }
    }

    default_Properties['properties'].update(sheetProperties)
    return default_Properties

def make_sheet(sheet_name):
    service = build('sheets', 'v4', credentials=creds)
    request_body = {
       'requests': [
           {
           'addSheet': sheetProperties(sheet_name)
           }
           ]
               }
    response = service.spreadsheets().batchUpdate(
               spreadsheetId=INDIVIUAL_SPREADSHEET_ID,
               body=request_body).execute()
    print(f"New sheet created: {response}")

