risultati ottenuti con prodLDA e LDA.
results html contiene i 6 modelli LDA migliori selezionati, ognuno con dei difetti:
- 7 topic e 70 epoche (corrisponde anche al miglior c_v per i 7 topic): Mancanze notate:  non riesco a capire cosa vuole rappresentare con un paio di topic
- 8 topic e 70 epoche (corrisponde anche alla miglior c_v per gli 8 topic).  Mancanze che ho notato: nessun topic descrive la situazione border/immigrants
- 8 topic e 150 epoche: questo mi sembra un buon modello, però anche qui fa un po' fatica a rappresentare border/immigrants
- 9 topic e 70 epoche (corrisponde anche al miglior c_v per i 9 topic). Questo è il miglior modello per quanto riguarda l'intersezione dei topic (non c'è nessuna sovrapposizione), rimane un po' assente il tema aborto/guerra
- 10 topic e 110 epoche: in questo caso non appare molto il topic relativo alla guerra (russia/ucraina/israele)
- 11 topic e 10 epoche: qui appare qualche topic più specifico ma scompare il discorso aborto/leggi sulle armi

Il modello migliore poi scelto per proseguire con le analisi è 8 topic con 150 epoche
- Nomi dei topic assegnati:
    nomi dei topic sono stati scegli sulla base delle parole più presenti in ognuno e sono:
        1: "American/economics/health",
        2: "War",
        3: "News/radio/livestream",
        4: "Republicans vs democrats",
        5: "Border/community/family",
        6: "Election/debate",
        7: "Abortion/rights/guns",
        8: "Infrastructure/job/energy",

- poi ogni tweet è stato classificato con il topic corretto e sono stati salvati in un file con i seguenti valori
    username: username dell’utente
    date: timestamp
    first_topic: topic assegnato (da 1 a 8)
    first_topic_name: nome del topic assegnato
    first_topic_prob: probabilità del topic assegnato
    second_topic: indica il secondo topic assegnato (da 1 a 8) (questo NON è sempre presente)
    second_topic_name: indica il nome del secondo topic assegnato
    second_topic_prob: indica la probabilità del secondo topic
    text: testo del tweet non pulito
    lemmatized_text: testo del tween con applicato lemming
    per_word_topics: indica i due topic più probabili per ogni parola del tweet con il loro numero (sempre da 1 a 8)
    per_word_topics_name: indica i due topic più probabili per ogni parola del tweet con il loro nome


