import gspread
import pandas as pd
from google.oauth2.service_account import Credentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
scopes = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']

credentials = Credentials.from_service_account_file('req-bot-2a5613e4841f.json', scopes=scopes)

gc = gspread.authorize(credentials)

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

# open a google sheet
gs = gc.open_by_key('16RpptPNwfL5sexVf3CdVWViNfpy_Y6z8VHnStJaCrvM')
# select a work sheet from its name
worksheet1 = gs.worksheet("Лист1")

# df = pd.DataFrame({'a': ['apple','airplane','alligator'], 'b': ['banana', 'ball', 'butterfly'], 'c': ['cantaloupe', 'crane', 'cat']})
# # write to dataframe
# worksheet1.clear()
# set_with_dataframe(worksheet=worksheet1, dataframe=df, include_index=False,
# include_column_header=True, resize=True)

df = pd.DataFrame({'foya':['jsgklfdsafse', 'ауыфаыуа'], 'fs':['aaefe', 'sfeasfa']})
df_values = df.values.tolist()
gs.values_append("Лист1", {'valueInputOption': 'RAW'}, {'values': df_values})