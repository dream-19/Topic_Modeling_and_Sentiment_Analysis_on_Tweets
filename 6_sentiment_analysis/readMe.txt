Come sentimental analysis è stato eseguito:
- sentiment analysis (positive, neutral, negative)
- emotion recognition  (anger, optimism, anticipation, joy, disgust, fear, sadness, surprise, love, pessimism, trust)
- hate speech detection (hate, not-hate)
- offensive language identification (offensive, non-offensive)


cartella grafici: contiene alcuni grafici dei risultati ottenuti
tools per sentimental analysis: elenco di possibili tool da usare, da cui poi è stato selezionato tweetNLP
sentiment_analysis.ipynb e sentiment_analysis_charts.ipynb: file jupyter con cui sono stati ottenuti i risultati

I risultati della sentiment analysis sono stati salvati su sentiment_analysis_all.csv: file csv che contiene l’applicazione della sentiment analysis su tutti i tweet (ordinato in modo crescente sulla base dell’emozione).
Indice del file:
username: username dell’utente
date: timestamp
first_topic: topic assegnato (da 1 a 8)
first_topic_name: nome del topic assegnato
first_topic_prob: probabilità del topic assegnato
sentiment: sentimento assegnato (positive, neutral, negative)
sentiment_prob: probabilità del sentimento assegnato
all_sentiments: probabilità di ogni sentimento
emotion: emozione assegnata (anger, optimism, anticipation, joy, disgust, fear, sadness, surprise, love, pessimism, trust)
emotion_prob: probabilità dell’emozione assegnata
all_emotions: probabilità di ogni emozione
hate: indica se c’è odio (hate, not-hate)
hate_prob: probabilità 
all_hate: probabilità di tutto, sia hate che not-hate
offensive: indica se è offensivo (offensive, non-offensive)
offensive_prob: indica la probabilità
all_offensive: probabilità di tutto (offensive e non-offensive)
second_topic: indica il secondo topic assegnato (da 1 a 8)
second_topic_name: indica il nome del secondo topic assegnato
second_topic_prob: indica la probabilità del secondo topic
text: testo del tweet non pulito
lemmatized_text: testo del tween con applicato lemming
per_word_topics: indica i due topic più probabili per ogni parola del tweet con il loro numero
per_word_topics_name: indica i due topic più probabili per ogni parola del tweet con il loro nome

