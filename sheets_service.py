import os
import json
import gspread

from oauth2client.service_account import ServiceAccountCredentials

SCOPES = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

def connect_google_sheets():

    if os.path.exists("credentials.json"):

        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "credentials.json",
            SCOPES
        )

    else:

        credentials_info = json.loads(
            os.getenv("GOOGLE_CREDENTIALS")
        )

        creds = ServiceAccountCredentials.from_json_keyfile_dict(
            credentials_info,
            SCOPES
        )

    return gspread.authorize(creds)

def get_sheet(sheet_name, worksheet_name):

    client = connect_google_sheets()

    spreadsheet = client.open(sheet_name)

    return spreadsheet.worksheet(worksheet_name)
