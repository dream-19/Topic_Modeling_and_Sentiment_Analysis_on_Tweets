import asyncio
from twscrape import API, gather
import pandas as pd
from datetime import datetime
import os


async def get_word_tweet(api, word, limit):
    all_tweet = await gather(api.search(word, limit=limit)) 
    print("Tweet trovati con ",word, ":", len(all_tweet))
    return all_tweet
    
    
async def get_user_tweet(api, user, user_id, limit): #https://tweeterid.com/
    await api.user_by_id(user_id)  # User

    all_tweet = await gather(api.user_tweets(user_id, limit=limit))
    print("Tweet trovati con ",user,':', len(all_tweet))
    return all_tweet

def show_tweets(all_tweet):
    for x in all_tweet: 
        print("------------------TWEET------------------")
        print( x.user.username, x.date, x.rawContent)
       
    
def convert_to_csv(all_tweet, theme):
    db = pd.DataFrame(columns=['username',
                                   'orario',
                                    'text'])
    for x in all_tweet: 
        username = '@'+ x.user.username
        orario = x.date
        text = x.rawContent
        iesimo_tweet = [username, orario, text]
        db.loc[len(db)] = iesimo_tweet #appendo il tweet al dataframe
        
    current_datetime = datetime.now()
    # Format the current datetime as a string with a timestamp
    today = current_datetime.strftime("%Y-%m-%d_%H:%M:%S")
    
    filename = f'{theme}_{today}.csv'
    print('filename',filename)
    db.to_csv(f'./files/{filename}')
    

async def main():
    api = API()
    await api.pool.add_account("facilina1", "megafacilina", "dreamviola19@gmail.com", "facilina123!") #Possono essere aggiunti più account
    await api.pool.login_all()
    
    print('avvio\n---------------------------------------------------')
    #Avvio le ricerche
    
    #1) @marwilliamson
    user = '@marwilliamson'
    result = await get_user_tweet(api,user, 21522338, 1)
    #show_tweets(result)
    convert_to_csv(result, user)
    
    #2) @Mike_Pence
    user = '@Mike_Pence'
    result = await get_user_tweet(api, user, 22203756, 1)
    #show_tweets(result)
    convert_to_csv(result, user)
    
    #3) #Democrats
    word = '#Democrats'
    result = await get_word_tweet(api, word, 1)
    show_tweets(result)
    convert_to_csv(result, word)
    

    print('---------------------------------------------------------\nfine!')
   
 
    

    
if __name__ == "__main__":
    asyncio.run(main())
    