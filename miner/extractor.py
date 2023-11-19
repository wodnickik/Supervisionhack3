import os
import re
from img2table.document import PDF
from img2table.ocr import TesseractOCR
import os
import pandas as pd
import numpy as np
from datetime import datetime


def read_deposit_len(time_str):
    time_str_split = time_str.split(" ")
    numb = int(time_str_split[0])
    if time_str_split[1][0] == 't':
        numb = numb/4

    return numb


def get_new_row(df, row, col, bank_name, date):
    bank = bank_name
    nazwa_oferty = "Lokata"
    oprocentowanie = df.iloc[row, col]
    typ_oferty = "Lokata"
    dlugosc_miesc = read_deposit_len(str(df.index[row]))
    typ_klienta = "Indywidualny"
    rodzaj_oferty = ""
    min_srodki = np.NaN
    max_srodki = np.NaN
    waluta = df.columns[col]
    uwagi = ""
    wazne_od = datetime.strptime(date, "%d-%m-%Y")

    return [bank, nazwa_oferty, oprocentowanie, typ_oferty, dlugosc_miesc,
            typ_klienta, rodzaj_oferty, min_srodki, max_srodki, waluta, uwagi, wazne_od]


def extract_data_from_table(df, bank_name, date):

    tmp = []
    df_final = pd.DataFrame()
    for row in range(df.shape[0]):
        for col in range(df.shape[1]):
            row_fill = get_new_row(df, row, col, bank_name, date)
            tmp.append(row_fill)
    df_final = pd.DataFrame(tmp, columns = ["Bank", "Nazwa oferty", "Oprocentowanie", "Typ oferty",
                                       "Długość (miesiące)", "Typ klienta", "Rodzaj oferty",
                                       "Minimalne środki", "Maksymalne środki", "Waluta",
                                       "Uwagi", "Ważne od"])    
    return df_final


if __name__ == "__main__":

    ocr = TesseractOCR(lang="pol")
    downloads_dir = '../downloads/'
    for bank in os.listdir(downloads_dir):
        for file in os.listdir(os.path.join(downloads_dir, bank)):
            if re.search('lokat', file, re.IGNORECASE) and re.search('\d\d-\d\d-\d\d\d\d', file):
                pdf = PDF(src=os.path.join(downloads_dir, bank, file))
                print(os.path.join(downloads_dir, bank, f'{file[:-4]}.xlsx'))
                
                if not os.path.isdir(os.path.join(downloads_dir, bank, 'output')):
                        os.mkdir(os.path.join(downloads_dir, bank, 'output'))
                pdf.to_xlsx(os.path.join(downloads_dir, bank, 'output', f'{file[:-4]}.xlsx'), ocr=ocr)
                
                date = re.search('\d\d-\d\d-\d\d\d\d', file).group(0)
                df = pd.read_excel(os.path.join(downloads_dir, bank, 'output', f'{file[:-4]}.xlsx'), 
                   header=[0], 
                   index_col=[0])
    
                print(extract_data_from_table(df, bank_name=bank, date=date))