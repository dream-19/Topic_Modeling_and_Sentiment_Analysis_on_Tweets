LDA (https://radimrehurek.com/gensim/models/ldamodel.html )
L’algoritmo LDA è stato usato sui dati pre-processati, in forma di una matrice tf-idf, provando a suddividere per n.topic = 5,6,7,8,9,10,11 e addestrando ogni volta sulle seguenti epoche: 1,5,10,20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 150, 200, 250, 300, 350.
Su ognuno di questi modelli è stato calcolato c_v, c_umass, c_uci e c_npmi (risultati dei grafici)

