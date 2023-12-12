Lo scraper usa il pkt  twscrape per funzionare: https://github.com/vladkens/twscrape

1) Installare i pkt necessari
pip install twscrape #(python >= 3.10)
pip install pandas

Esecuzione file: python3 scraper.py

2) Per poter usare un twscrape bisogna avere un account twitter che deve essere inserito nel file, incluso di mail utilizzata e di password della mail
await api.pool.add_account("nome_account", "password_account", "email", "password_email!") 
Possono essere aggiunti più account per evitare blocchi di tempo

3) Scaricare Tweet:
è possibile scaricare sia tweets da account (in quel caso serve l'id dell'account) sia tweets in base a parole/hashtag.
Nel caso di tweet provenienti da un account vengono presi anche i tweet repostati.
Viene memorizzato il tweet retweettato con un RT di fronte e poi anche il tweet e l'account di provenienza (quindi appare due volte).
Es:
    1) Mike_Pence,2023-08-24 04:19:39+00:00,"RT @TeamPence: “I chose the Constitution, and I always will.” —@Mike_Pence #GOPDebate",
    2) TeamPence,2023-08-24 04:17:15+00:00,"“I chose the Constitution, and I always will.” —@Mike_Pence #GOPDebate",

Nel main vengono definiti i punti da cui prelevare i tweets.

Esempio da account:
user = '@marwilliamson'
result = await get_user_tweet(api,user, 21522338, 300) #api, nome user, id user, limite tweet

Esempio da parola:
#Democrats
word = '#Democrats'
result = await get_word_tweet(api, word, 300) #api, parole, limite tweet

Il limite dei tweet dovrebbe indicare i tweet massimi ma in realtà funziona parzialmente e ne da sempre più di quelli indicati

I tweet poi possono essere mostrati tramite la funzione show_tweets(result)

4) Scaricare i Tweet in un csv:
La funzione convert_to_csv(tutti_i_tweets, nome_file) permette di salvare il risultato in un csv (all'interno di ./files)
- Se il csv è già esistente allora i tweets vengono aggiunti in cima altrimenti si crea un nuovo file
- Se è specificato onlyToday=True allora salva nel csv solo i tweets del giorno corrente

