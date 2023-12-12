2 - text pre-processing
Esecuzione di pre-processing sui tweet raccolti per ottenere 70 000 tweet da utilizzare nel processamento effettivo. 

Passaggi eseguiti per il preprocessing:
Tutti i file di tweet sono stati riuniti nel file ‘merged.csv’ composto dalle colonne: username, date, text. Durante questa fase sono stati eliminati tutti i tweet non riconosciuti come lingua inglese tramite la libreria langdetect (raccolti nel file deleted_rows.csv)

Poi per ogni tweet del file ‘merged.csv’ sono stati eseguiti i seguenti passaggi:
rimozione di tutti gli url/hashtag/emoji/parole riservate da tweeter (es: RT)
rimozione di spazi inutili
testo in lowecase
normalizzazione della forma contratta (isn't in is not,...)
rimozione punteggiatura
rimozione numeri
rimozione stop word tramite l’uso del pacchetto di stopword di spacy (326 parole comuni) (estensione della lista originale con le parole comuni a questo set di tweet e con gli slang: [‘amp’,‘gets’,'breaking', 'report' ,'new', 'omg', 'lol', 'fyi', 'idk', 'brb', 'smh', 'asap', 'btw', 'gtg', 'nsfw', 'yolo', 'rofl', 'imo', 'imho'])
lemming  
stemming ( a partire dai tweet generati al punto 8., quindi non a seguito del lemming)
 Rimozione di caratteri singoli (sia dal testo che da lemming e stemming)
Rimozione di tweet che contengono un numero di caratteri inferiore o uguale a 5


Poi i tweet (tranne eventuali doppioni) sono stati salvati in un file ‘cleaned.csv’.


Il risultato finale ottenuto è di 70.000 tweet puliti pronti per il processamento 



