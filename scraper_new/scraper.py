import asyncio
from twscrape import API, gather
import pandas as pd
import datetime


async def get_user_tweet(api, user_id, limit): #https://tweeterid.com/
    await api.user_by_id(user_id)  # User

    all_tweet = await gather(api.user_tweets(user_id, limit=limit))
    return all_tweet

def show_tweets(all_tweet):
    num_tweet = 0
    for x in all_tweet: 
        print("------------------TWEET------------------")
        print( x.user.username, x.date, x.rawContent)
        num_tweet = num_tweet + 1
    
    print("numero tweet: ", num_tweet)
    
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
    today = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    filename = f'{theme}_{today}.csv'
    db.to_csv(f'./files/{filename}')
    

async def main():
    api = API()
    await api.pool.add_account("facilina1", "megafacilina", "dreamviola19@gmail.com", "facilina123!") #Possono essere aggiunti più account
    await api.pool.login_all()
    
    print('avvio\n---------------------------------------------------')
    #Avvio le ricerche
    
    #1) @marwilliamson
    result = await get_user_tweet(api, 21522338, 1)
    print(result)
    show_tweets(result)
    convert_to_csv(result, '@marwilliamson')
    
    #2) @Mike_Pence
    result = await get_user_tweet(api, 22203756, 1)
    show_tweets(result)
    convert_to_csv(result, '@Mike_Pence')
    
    
    print('---------------------------------------------------------\nfine!')
   
 
    

    
if __name__ == "__main__":
    asyncio.run(main())
    