import sys

import pandas as pd
import os


def file_merging(directory):
    db_output = pd.DataFrame(columns=['text'])
    i = 0

    try:
        file_path = os.path.join(os.getcwd(), directory)
    except Exception:
        print("Cartella non trovata")
        sys.exit(1)

    os.chdir(file_path)
    print(os.getcwd())
    for filename in os.listdir(os.getcwd()):
        print(filename)
        db = pd.read_csv(filename)
        for row in db.itertuples():
            nuovo_insert = [row.text]
            db_output.loc[len(db_output)] = nuovo_insert
            i = i + 1

    db_output.to_csv(f'{directory}_merged.csv')


def file_merging_with_date(directory):
    db_output = pd.DataFrame(columns=['orario',
                                      'text'])
    i = 0

    file_path = os.path.join(os.getcwd(), directory)

    os.chdir(file_path)
    print(os.getcwd())
    for filename in os.listdir(os.getcwd()):
        print(filename)
        db = pd.read_csv(filename)
        for row in db.itertuples():
            nuovo_insert = [row.orario, row.text]
            db_output.loc[len(db_output)] = nuovo_insert
            i = i + 1

    db_output.to_csv(f'{directory}_merged.csv', index=False)


if __name__ == '__main__':
    print("Indicare il nome della cartella in cui sono i file da unire: ")
    cartella = input()
    file_merging_with_date(cartella)
