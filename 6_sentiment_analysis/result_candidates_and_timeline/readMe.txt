Per ogni topic e per ogni candidato analizzato si mostra la sentiment analysis, emotion recognition, hate and offensive detection

Topic
    1: "American/economics/health",
    2: "War",
    3: "News/radio/livestream",
    4: "Republicans vs democrats",
    5: "Border/community/family",
    6: "Election/debate",
    7: "Abortion/rights/guns",
    8: "Infrastructure/job/energy",

Candidati da analizzare
    # democratici
    "marwilliamson": ("Marianne Williamson", "democratic"),
    "POTUS": ("Joe Biden", "democratic"),
   
    # repubblicani
    "NikkiHaley": ("Nikki Haley", "republican"),
    "RonDeSantis": ("Ron De Santis", "republican"),  

Sentimenti
neutral, negative, positive

Emozioni
anger, optimism, anticipation, joy, disgust, fear, sadness, surprise, love, pessimism, trust

Hate
hate, not-hate

Offensive
offensive. non-offensive

è stato generato un file csv per ogni topic ed ogni candidato con i seguenti campi (ordinato sulla base dell’emozione):
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

----------------------------

Per ogni topic si effettua sentiment analysis ed emotion analysis ogni 10 giorni a partire dal 06-03-2023 fino al 22-10-2023 (su tutti i tweet analizzati)

Topic
    1: "American/economics/health",
    2: "War",
    3: "News/radio/livestream",
    4: "Republicans vs democrats",
    5: "Border/community/family",
    6: "Election/debate",
    7: "Abortion/rights/guns",
    8: "Infrastructure/job/energy",

Sentimenti
neutral, negative, positive

Emozioni
anger, optimism, anticipation, joy, disgust, fear, sadness, surprise, love, pessimism, trust

Hate
hate, not-hate

Offensive
offensive. non-offensive

Ogni file csv generato (uno ogni 10 giorni e per ogni topic) ha il seguente indice ed è ordinato sulla base della data (in ordine crescente)
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

