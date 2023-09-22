import sys

import pandas as pd


def filtro_spam(filename):
    try:
        db = pd.read_csv(filename)
    except Exception:
        print("File non trovato")
        sys.exit(1)
    db_output = pd.DataFrame(columns=['username',
                                      'orario',
                                      'text'])
    i = 1

    df_spam = pd.read_csv("spam.csv")
    spam = 0

    for row in db.itertuples():
        for riga in df_spam.itertuples():
            if riga.text in row.text:
                spam = 1
                break
        if spam == 0:
            nuovo_insert = [row.username, row.orario, row.text]
            db_output.loc[len(db_output)] = nuovo_insert
            i = i+1
        spam = 0

    filter_filename = f'{filename}_spam.csv'
    db_output.to_csv(filter_filename)
    return filter_filename


def filtro_duplicati(filename):
    db = pd.read_csv(filename)
    db_output = pd.DataFrame(columns=['text'])
    i = 0
    lista = []

    for row in db.itertuples():
        lista.append(row.text)

    lista = list(dict.fromkeys(lista))
    for tweet in lista:
        nuovo_insert = [tweet]
        db_output.loc[len(db_output)] = nuovo_insert
        i = i + 1

    filter_filename = f'{filename}_dup1.csv'
    db_output.to_csv(filter_filename)
    return filter_filename


def filtro_duplicati_with_date(filename):
    db = pd.read_csv(filename)
    db_output = pd.DataFrame(columns=['orario',
                                      'text'])
    i = 0
    checklist = []
    lista = []

    for row in db.itertuples():
        if row.text not in checklist:
            checklist.append(row.text)
            lista.append((row.text, row.orario))

    for element in lista:
        nuovo_insert = [element[1], element[0]]
        db_output.loc[len(db_output)] = nuovo_insert
        i = i + 1

    filter_filename = f'{filename}_dup.csv'
    (db_output.sort_values(by='orario')).to_csv(filter_filename, index=False)
    return filter_filename


def add_id(filename):
    try:
        db = pd.read_csv(filename)
    except Exception:
        print("File non trovato")
        sys.exit(1)
    db_output = pd.DataFrame(columns=['ID',
                                      'DATE',
                                      'TEXT'])
    i = 1
    for row in db.itertuples():
        nuovo_insert = [i, row.orario, row.text]
        db_output.loc[len(db_output)] = nuovo_insert
        i = i + 1

    db_output.to_csv(f'{filename}_id.csv', index=False)


if __name__ == '__main__':
    print("Digitare 1 per eseguire filtering, 2 per aggiungere ID: ")
    select = input()
    if select == '1':
        print("Inserire il nome del file da filtrare: ")
        nome_file = input()
        spam_filter = filtro_spam(nome_file)
        filtro_duplicati_with_date(spam_filter)
    elif select == '2':
        print("Inserire il nome del file a cui aggiungere un ID: ")
        nome_file = input()
        add_id(nome_file)
    else:
        print("Input non valido")
