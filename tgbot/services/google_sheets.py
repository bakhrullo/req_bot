import gspread
import pandas as pd
from google.oauth2.service_account import Credentials


async def worksheet(**kwargs):
    scopes = ['https://www.googleapis.com/auth/spreadsheets',
              'https://www.googleapis.com/auth/drive']
    credentials = Credentials.from_service_account_file('req-bot-2a5613e4841f.json', scopes=scopes)
    gc = gspread.authorize(credentials)
    gs = gc.open_by_key('16RpptPNwfL5sexVf3CdVWViNfpy_Y6z8VHnStJaCrvM')
    df = pd.DataFrame({'No': [kwargs["no"]], 'Ism': [kwargs["name"]], 'Raqam': [kwargs["phone"]], 'Yo\'nalish': [kwargs["country"]],
                       'Mahsulot': [kwargs["prod"]], 'To\'lov qiymati': [kwargs["sum"]], 'To\'lov holati': [kwargs["sum_type"]],
                       'Pochta': [kwargs["pochta"]], 'Hudud': [kwargs["area"]], 'Tarmoq': [kwargs["social"]],
                       'Mutaxassis': [kwargs["operator"]], 'Yetkazib berish muddati': [kwargs["date"]], 'Manzil': [kwargs["address"]],
                       'Izoh': [kwargs["comm"]]})
    df_values = df.values.tolist()
    gs.values_append("Лист1", {'valueInputOption': 'RAW'}, {'values': df_values})
