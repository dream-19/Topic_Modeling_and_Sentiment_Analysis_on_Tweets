import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level

async def main():
    api = API()  # or API("path-to.db") - default is `accounts.db`

    # ADD ACCOUNTS (for CLI usage see BELOW)
    #await api.pool.add_account("facilina1", "megafacilina", "dreamviola19@gmail.com", "facilina123!")
    #await api.pool.add_account("user2", "pass2", "u2@example.com", "mail_pass2")
    await api.pool.login_all()

    # or add account with COOKIES (with cookies login not required)
    #cookies = "abc=12; ct0=xyz"  # or '{"abc": "12", "ct0": "xyz"}'
    #await api.pool.add_account("user3", "pass3", "u3@mail.com", "mail_pass3", cookies=cookies)

    # add account with PROXY
    #proxy = "http://login:pass@example.com:8080"
    #await api.pool.add_account("user4", "pass4", "u4@mail.com", "mail_pass4", proxy=proxy)

    # API USAGE

    # search (latest tab)
    #await gather(api.search("marwilliamson", limit=20))  # list[Tweet]

    # tweet info
    #tweet_id = 20
    #await api.tweet_details(tweet_id)  # Tweet
    #await gather(api.retweeters(tweet_id, limit=20))  # list[User]
    #await gather(api.favoriters(tweet_id, limit=20))  # list[User]

    '''# get user by login
    user_login = "xdevelopers"
    await api.user_by_login(user_login)  # User
    '''

    # user info
    user_id = 22203756 #21522338
    await api.user_by_id(user_id)  # User
    #await gather(api.followers(user_id, limit=20))  # list[User]
    #await gather(api.following(user_id, limit=20))  # list[User]
    #await gather(api.user_tweets(user_id, limit=2))  # list[Tweet]
    #await gather(api.user_tweets_and_replies(user_id, limit=20))  # list[Tweet]
    ind = 0
    result = await gather(api.user_tweets(user_id, limit=1))
    for x in result: 
        print("------------------TWEET------------------")
        print( x.user.username, x.date, x.rawContent)
        ind = ind + 1
       
        
    print("numero tweet: ", ind)
 
    

    '''
    print('ciao')
    q = "marwilliamson since:2023-09-20 until:2023-09-22"
    async for tweet in api.search(q, limit=5):
        print(tweet.id, tweet.user.username, tweet.rawContent)
    '''
    print('fine')
    
if __name__ == "__main__":
    asyncio.run(main())
    