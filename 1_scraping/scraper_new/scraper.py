import asyncio
from twscrape import API, gather
import pandas as pd
from datetime import datetime, timedelta
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
        print( x.user.username, x.date + timedelta(hours=2), x.rawContent)
       
    
def convert_to_csv(all_tweet, theme, onlyToday = False):
    db = pd.DataFrame(columns=['username',
                                   'orario',
                                    'text'])
    
    today = datetime.now().date() 
    for x in all_tweet: 
        username = x.user.username
        orario = x.date + timedelta(hours=2) #correzione orario (UTC+2)
        text = x.rawContent
        iesimo_tweet = [username, orario, text]

        if onlyToday:
            # Check if the timestamp's date is the same as the current date
            if orario.date() != today:
                continue #skip the tweet
            
        db.loc[len(db)] = iesimo_tweet #appendo il tweet al dataframe
        
    #Creazione del file
    filename = f'./files/{theme}.csv'

    # Check if the file exists
    if os.path.isfile(filename):
        #Append of results
        # Define the path to the existing CSV file
        existing_csv_file = filename

        # Read the existing CSV file into a DataFrame
        existing_df = pd.read_csv(existing_csv_file)
        
        #Se per un qualche motivo c'è una quarta colonna (errore), la elimino
        num_columns = existing_df.shape[1]

        # Check if there are at least 4 columns before attempting to delete the fourth one
        if num_columns >= 4:
            existing_df.drop(existing_df.columns[3], axis=1, inplace=True)
        
        # Concatenate the new DataFrame with the existing one while preserving the index
        final_df = pd.concat([db, existing_df], ignore_index=True) #append on top for the new results

        # Overwrite the existing CSV file with the concatenated DataFrame
        final_df.to_csv(existing_csv_file, index=False)
    else:
        #Create new result file
        db.to_csv(filename)
    
    print("New Tweets saved in file:", len(db))
    

async def main():
    api = API() #Possono essere aggiunti più account
    await api.pool.add_account("carol", "xxxx", "carolina432_@libero.it", "xxx")
    await api.pool.add_account("cosim", "xxxx", "cosima000@libero.it", "xxx")
    await api.pool.login_all()
    
    print('Avvio\n---------------------------------------------------')
    #Avvio le ricerche
    
    #Candidati
    #1) @marwilliamson
    user = '@marwilliamson'
    result = await get_user_tweet(api,user, 21522338, 100)
    #show_tweets(result)
    convert_to_csv(result, user, True)
    
    #2) @Mike_Pence
    user = '@Mike_Pence'
    result = await get_user_tweet(api, user, 22203756, 100)
    #show_tweets(result)
    convert_to_csv(result, user, True)
    
    #3) #Democrats
    word = '#Democrats'
    result = await get_word_tweet(api, word, 800)
    #show_tweets(result)
    convert_to_csv(result, word, True)
    
    #4) #Republicans
    word = '#Republicans'
    result = await get_word_tweet(api, word, 800)
    #show_tweets(result)
    convert_to_csv(result, word, True)
    
    #5) @TheDemocrats
    user = '@TheDemocrats'
    result = await get_user_tweet(api, user, 14377605, 200)
    #show_tweets(result)
    convert_to_csv(result, user, True)
    
    #6) @GOP
    user = '@GOP'
    result = await get_user_tweet(api, user, 11134252, 200)
    convert_to_csv(result, user, True)
    
    #7) @AP_Politics
    user = '@AP_Politics'
    result = await get_user_tweet(api, user, 426802833, 100)
    convert_to_csv(result, user, True)
    
    #8) @politico
    user = '@politico'
    result = await get_user_tweet(api, user, 9300262, 100)
    convert_to_csv(result, user, True)
    
    #9) @POTUS
    user = '@POTUS'
    result = await get_user_tweet(api, user, 1349149096909668363, 100)
    convert_to_csv(result, user, True)
    
    #10) @RobertKennedyJr
    user = '@RobertKennedyJr'
    result = await get_user_tweet(api, user, 337808606, 100)
    convert_to_csv(result, user, True)
    
    #11) @NikkiHaley
    user = '@NikkiHaley'
    result = await get_user_tweet(api, user, 1079776144524754944, 100)
    convert_to_csv(result, user, True)
    
    #12) @VivekGRamaswamy
    user = '@VivekGRamaswamy'
    result = await get_user_tweet(api, user, 1227799690579718144, 100)
    convert_to_csv(result, user, True)
    
    #13) @PJQualityGuru
    user = '@PJQualityGuru'
    result = await get_user_tweet(api, user, 1485738434098601989, 100)
    convert_to_csv(result, user, True)
    
    #14) @larryelder
    user = '@larryelder'
    result = await get_user_tweet(api, user, 195271137, 100)
    convert_to_csv(result, user, True)
    
    #15) @RyanBinkley
    user = '@RyanBinkley'
    result = await get_user_tweet(api, user, 39279015, 100)
    convert_to_csv(result, user, True)
    
    #16) @Senatortimscott
    user = '@Senatortimscott'
    result = await get_user_tweet(api, user, 217543151, 100)
    convert_to_csv(result, user, True)
    
    #17)@RonDeSantis
    user = '@RonDeSantis'
    result = await get_user_tweet(api, user, 487297085, 100)
    convert_to_csv(result, user, True)
    
    #18) @GovChristie
    user = '@GovChristie'
    result = await get_user_tweet(api, user, 90484508, 100)
    convert_to_csv(result, user, True)
    
    #19) @GovDougBurgum
    user = '@GovDougBurgum'
    result = await get_user_tweet(api, user, 518700708, 100)
    convert_to_csv(result, user, True)
   
    #20) @WillHurd
    user = '@WillHurd'
    result = await get_user_tweet(api, user, 2963445730, 100)
    convert_to_csv(result, user, True)
    
    
    #21) @HouseGOP
    user = '@HouseGOP'
    result = await get_user_tweet(api, user, 15207668, 100)
    convert_to_csv(result, user, True)
    
    #22) @SenateGOP
    user = '@SenateGOP'
    result = await get_user_tweet(api, user, 14344823, 100)
    convert_to_csv(result, user, True)
    
    #23) @HouseDemocrats
    user = '@HouseDemocrats'
    result = await get_user_tweet(api, user, 43963249, 100)
    convert_to_csv(result, user, True)
    
    #24) @dscc
    user = '@dscc'
    result = await get_user_tweet(api, user, 14466538, 100)
    convert_to_csv(result, user, True)
    
    #Altri politici interessanti:
    #1) @KamalaHarris
    user = '@KamalaHarris'
    result = await get_user_tweet(api, user, 30354991, 100)
    convert_to_csv(result, user, True)
    
    #2) @MichaelBennet
    user = '@MichaelBennet'
    result = await get_user_tweet(api, user, 45645232, 100)
    convert_to_csv(result, user, True)
    
    #3) @SecretaryPete
    user = '@SecretaryPete'
    result = await get_user_tweet(api, user, 1356958547603513346, 100)
    convert_to_csv(result, user, True)
    
    #4) @JohnDelaney
    user = '@JohnDelaney'
    result = await get_user_tweet(api, user, 426028646, 100)
    convert_to_csv(result, user, True)
    
    #5) @TulsiGabbard
    user = '@TulsiGabbard'
    result = await get_user_tweet(api, user, 26637348, 100)
    convert_to_csv(result, user, True)
    
    #6) @gillibrandny
    user = '@gillibrandny'
    result = await get_user_tweet(api, user, 899978622416695297, 100)
    convert_to_csv(result, user, True)
    
    #7) @SenatorHick
    user = '@SenatorHick'
    result = await get_user_tweet(api, user, 1318728336923787264, 100)
    convert_to_csv(result, user, True)
    
    #8) @SenAmyKlobuchar
    user = '@SenAmyKlobuchar'
    result = await get_user_tweet(api, user, 22044727, 100)
    convert_to_csv(result, user, True)
    
    #9) @BernieSanders
    user = '@BernieSanders'
    result = await get_user_tweet(api, user, 216776631, 100)
    convert_to_csv(result, user, True)
    
    #10) @SenWarren
    user = '@SenWarren'
    result = await get_user_tweet(api, user, 970207298, 100)
    convert_to_csv(result, user, True)
    
    #11) @AndrewYang
    user = '@AndrewYang'
    result = await get_user_tweet(api, user, 2228878592, 100)
    convert_to_csv(result, user, True)
    
    #12)@TomSteyer
    user = '@TomSteyer'
    result = await get_user_tweet(api, user, 949934436, 100)
    convert_to_csv(result, user, True)
    
    #13) @SenDuckworth
    user = '@SenDuckworth'
    result = await get_user_tweet(api, user, 1058520120, 100)
    convert_to_csv(result, user, True)
    
    #14) @valdemings
    user = '@valdemings'
    result = await get_user_tweet(api, user, 3404875323, 100)
    convert_to_csv(result, user, True)
    
    #15) @BarackObama
    user = '@BarackObama'
    result = await get_user_tweet(api, user, 813286, 100)
    convert_to_csv(result, user, True)
    
    
    #16) @GovMLG
    user = '@GovMLG'
    result = await get_user_tweet(api, user, 1070083706822438912, 100) 
    convert_to_csv(result, user, True)
    
    #17) @SenatorBaldwin
    user = '@SenatorBaldwin'
    result = await get_user_tweet(api, user, 1074518754, 100)
    convert_to_csv(result, user, True)
    
    #18) @SenatorHassan
    user = '@SenatorHassan'
    result = await get_user_tweet(api, user, 946549322, 100)
    convert_to_csv(result, user, True)
    
    #19) @GovWhitmer
    user = '@GovWhitmer'
    result = await get_user_tweet(api, user, 102071743, 100)
    convert_to_csv(result, user, True)
    
    
    #20) @SpeakerMcCarthy
    user = '@SpeakerMcCarthy'
    result = await get_user_tweet(api, user, 19739126, 100)
    convert_to_csv(result, user, True)
    
    #21) @laurenboebert
    user = '@laurenboebert'
    result = await get_user_tweet(api, user, 1201670995435646976, 100)
    convert_to_csv(result, user, True)
    
    #22) @Jim_Jordan
    user = '@Jim_Jordan'
    result = await get_user_tweet(api, user, 18166778, 100)
    convert_to_csv(result, user, True)
    
    #23) @RepSpanberger
    user = '@RepSpanberger'
    result = await get_user_tweet(api, user, 1078771401497161728, 100)
    convert_to_csv(result, user, True)
    
    
    #24) @RepSherrill
    user = '@RepSherrill'
    result = await get_user_tweet(api, user, 1080569698536878081, 100)
    convert_to_csv(result, user, True)
    
    #25) @RepSlotkin
    user = '@RepSlotkin'
    result = await get_user_tweet(api, user, 1078401427347857408, 100)
    convert_to_csv(result, user, True)
    
    #26) @RepHoulahan
    user = '@RepHoulahan'
    result = await get_user_tweet(api, user, 1052896620797460481, 100)
    convert_to_csv(result, user, True)
    
    
    
    #Account giornalistici:
    #1) @MollyJongFast
    user = '@MollyJongFast'
    result = await get_user_tweet(api, user, 14298769, 100)
    convert_to_csv(result, user, True)
    
    #2)@jamesrhenson
    user = '@jamesrhenson'
    result = await get_user_tweet(api, user, 49758766, 100)
    convert_to_csv(result, user, True)
    
    #3) @NewsbySmiley
    user = '@NewsbySmiley'
    result = await get_user_tweet(api, user, 250690720, 100)
    convert_to_csv(result, user, True)
    
    #4) @jonathanvswan
    user = '@jonathanvswan'
    result = await get_user_tweet(api, user, 327862439, 100)
    convert_to_csv(result, user, True)
    
    #5) @rickhasen
    user = '@rickhasen'
    result = await get_user_tweet(api, user, 47034524, 100)
    convert_to_csv(result, user, True)
    
    #6) @amyewalter
    user = '@amyewalter'
    result = await get_user_tweet(api, user, 50073507, 100)
    convert_to_csv(result, user, True)
    
    #7) @Redistrict
    user = '@Redistrict'
    result = await get_user_tweet(api, user, 74820061, 100)
    convert_to_csv(result, user, True)
    
    #8) @CookPolitical
    user = '@CookPolitical'
    result = await get_user_tweet(api, user, 191477653, 100)
    convert_to_csv(result, user, True)
    
    #9) @Nate_Cohn
    user = '@Nate_Cohn'
    result = await get_user_tweet(api, user, 463765807, 100)
    convert_to_csv(result, user, True)
    
    #10) @NateSilver538
    user = '@NateSilver538'
    result = await get_user_tweet(api, user, 16017475, 100)
    convert_to_csv(result, user, True)
    
    #Altri hashtag interessanti:
    #1) #uspolitics
    word = '#uspolitics'
    result = await get_word_tweet(api, word, 300)
    convert_to_csv(result, word, True)
    
    #2) #US2024election
    word = '#US2024election'
    result = await get_word_tweet(api, word, 100)
    convert_to_csv(result, word, True)
    
    #3) #uselection2024
    word = '#uselection2024'
    result = await get_word_tweet(api, word, 100)
    convert_to_csv(result, word, True)
    
    #4) #DEMOCRACY24
    word = '#DEMOCRACY24'
    result = await get_word_tweet(api, word, 500)
    convert_to_csv(result, word, True)
    
    #5) #Trump2024
    word = '#Trump2024'
    result = await get_word_tweet(api, word, 500)
    convert_to_csv(result, word, True)
    
    #6) #Biden2024
    word = '#Biden2024'
    result = await get_word_tweet(api, word, 500)
    convert_to_csv(result, word, True)
    
    
    #Altro:
    #1) '@LeadingReport'
    user = '@LeadingReport'
    result = await get_user_tweet(api, user, 1528943647185678336, 150)
    convert_to_csv(result, user, True)
    
    #2) @IngrahamAngle
    user = '@IngrahamAngle'
    result = await get_user_tweet(api, user, 50769180, 100)
    convert_to_csv(result, user, True)
    
    #3) @marklevinshow
    user = '@marklevinshow'
    result = await get_user_tweet(api, user, 38495835, 100)
    convert_to_csv(result, user, True)
    
    #4) @CollinRugg
    user = '@CollinRugg'
    result = await get_user_tweet(api, user, 890061634181373952, 100)
    convert_to_csv(result, user, True)
    
    #5) @TheDemCoalition
    user = '@TheDemCoalition'
    result = await get_user_tweet(api, user, 713839291210792960, 100)
    convert_to_csv(result, user, True)
    
    #6) @WhiteHouse
    user = '@WhiteHouse'
    result = await get_user_tweet(api, user, 1323730225067339784, 100)
    convert_to_csv(result, user, True)
    
    #7) @WashTimesOpEd
    user = '@WashTimesOpEd'
    result = await get_user_tweet(api, user, 41207697, 100)
    convert_to_csv(result, user, True)
    
    #8) @NRSC
    user = '@NRSC'
    result = await get_user_tweet(api, user, 5693842, 100)
    convert_to_csv(result, user, True)
    
    
    print('---------------------------------------------------------\nfine!')
   
 

    
if __name__ == "__main__":
    asyncio.run(main())
    