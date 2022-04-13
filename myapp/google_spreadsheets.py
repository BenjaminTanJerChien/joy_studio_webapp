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
SERVICE_ACCOUNT_FILE = r'/keys/key.json'
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

