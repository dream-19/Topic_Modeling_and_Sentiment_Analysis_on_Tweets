import tweepy
import pandas as pd
import datetime


class Scraper():
    def __init__(self):
        self.consumer_key = "------"
        self.consumer_secret = "-----"
        self.access_token = "---"
        self.access_token_secret = "----"
        self.callback_uri = 'oob'

    def start(self):
        print("AVVIO APPLICAZIONE PER LA RICERCA DI TWEET")

    def printtweetdata(self, n, iesimo_tweet):
        print()
        print(f"Tweet {n}:")
        print(f"Username:{iesimo_tweet[0]}")
        print(f"Orario:{iesimo_tweet[1]}")
        print(f"Tweet Text:{iesimo_tweet[2]}")

    def scrape(self, parole, data, num_tweets):

        db = pd.DataFrame(columns=['username',
                                   'orario',
                                    'text'])

        tweets = tweepy.Cursor(self.api.search_tweets, parole, lang="it", tweet_mode="extended").items(num_tweets)
        #tweets = self.api.user_timeline(screen_name='@marwilliamson', count=1)

        list_tweets = [tweet for tweet in tweets]

        i = 1

        for tweet in list_tweets:
            username = tweet.user.screen_name
            orario = tweet.created_at

            try:
                text = tweet.retweeted_status.full_text
            except AttributeError:
                text = tweet.full_text

            iesimo_tweet = [username, orario, text]
            db.loc[len(db)] = iesimo_tweet

            self.printtweetdata(i, iesimo_tweet)
            i = i+1
        filename = f'{parole}_{data}.csv'

        db.to_csv(filename)

    def execution(self, hashtag, nome):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(auth, wait_on_rate_limit=True)

        numtweet = 100
        self.scrape(hashtag, nome, numtweet)
        print("Scraping completato.")


if __name__ == '__main__':
    ricerca = Scraper()
    auth = tweepy.OAuthHandler(ricerca.consumer_key, ricerca.consumer_secret)
    auth.set_access_token(ricerca.access_token, ricerca.access_token_secret)
    ricerca.api = tweepy.API(auth, wait_on_rate_limit=True)

    #print("Inserire hashtag sul quale effettaure la ricerca: ")
    #hashtag = input()
    #print("Inserire la data nel formato yyyy-mm-dd: ")
    #date_since = input()
    
    hashtag = "#love"
    date_since =  datetime.date.today()
    
    numtweet = 1
    ricerca.scrape(hashtag, date_since, numtweet)
    print("Scraping completato.")
    
    
# Ho modificato la data, è presa in automatico