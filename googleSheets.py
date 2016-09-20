
import json
import os
import requests
import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials



scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('My Project-e08df21666bc.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("prueba1")

#ht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1jJlMj_FsxREqV8VYGByV4RhpS5LoEoOz_3nYzbQMz1M/pubhtml')

worksheet = wks.worksheet("gestionados")

cliente = worksheet.find("GESTAMP")
servicio = worksheet.find("S. Gestionado")

column = cliente.col
row = servicio.row

valorBuscado = worksheet.cell(row, column).value

print(valorBuscado)