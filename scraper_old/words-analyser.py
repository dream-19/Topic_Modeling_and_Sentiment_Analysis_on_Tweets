import sys
import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer


def clear_words(filename):
    try:
        db = pd.read_csv(filename)
    except Exception:
        print("File non trovato")
        sys.exit(1)
    db_output = pd.DataFrame(columns=['ID',
                                      'TEXT'])

    for row in db.itertuples():
        text = row.TEXT
        frase = re.sub('http[s]?://\S+', '', text)
        stop_words = stopwords.words('italian')
        stop_words.extend(['secondadose', 'terzadose', 'booster', 'vaccino', 'Booster', 'covid', 'covid19'])
        tokenizer = RegexpTokenizer(r'\w+')
        word_tokens = tokenizer.tokenize(frase)
        filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
        filtered_sentence = []

        for w in word_tokens:
            if w.lower() not in stop_words:
                filtered_sentence.append(w)

        nuovo_insert = [row.ID, filtered_sentence]
        db_output.loc[len(db_output)] = nuovo_insert

    output_filename = f"{filename}_token.csv"
    db_output.to_csv(output_filename, index=False)
    return output_filename


def count_words(filename):
    frequency = {}
    lista_id = {}
    db = pd.read_csv(filename)
    db_output = pd.DataFrame(columns=['FREQUENZA',
                                      'PAROLA',
                                      'TWEET ID'])
    i = 0

    for row in db.itertuples():
        testo = (((((row.TEXT).replace('[', '')).replace(']', '')).replace('\'', '')).replace(' ', ''))
        lista = list(testo.split(','))
        for item in lista:
            if item in frequency:
                frequency[item] += 1
                lista_id[item].append(str(row.ID))
            else:
                frequency[item] = 1
                lista_id[item] = [str(row.ID)]

    for element in frequency:
        if frequency[element] > 2:
            identificativi = (((str(lista_id[element]).replace('[', '')).replace(']', '')).replace('\'', ''))
            nuovo_insert = [frequency[element], element, identificativi]
            db_output.loc[len(db_output)] = nuovo_insert
            i = i + 1
    (db_output.sort_values(by='FREQUENZA', ascending=False)).to_csv(f"{filename}_words_count.csv", index=False)


if __name__ == '__main__':
    print("Inserire il nome del file di cui si esegue il word count: ")
    nome_file = input()
    clear_file = clear_words(nome_file)
    count_words(clear_file)
