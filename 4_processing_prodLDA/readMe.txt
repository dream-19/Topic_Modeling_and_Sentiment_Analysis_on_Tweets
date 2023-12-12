prodLDA (https://pyro.ai/examples/prodlda.html )
L’algoritmo prodLDA è stato usato sui dati pre-processati in forma di una matrice tf-idf, provando a suddividere per n.topic = 5,6,7,8,9,10 e addestrando ognuno per 50 epoche, con learning rate 1e-3 e batch size di 32. Poi i modelli sono stati valutati sulle stesse misure di coerenza del LDA, ottenendo valori abbastanza simili.
