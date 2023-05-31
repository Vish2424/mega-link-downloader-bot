import os

class Config(object):
    TG_BOT_TOKEN = "5135540517:AAF75sRjRjq_MQTDfhitGlkZYnbB00a8GGE"
    
    APP_ID = 16620990
    
    API_HASH = d684f9b645ea3b73e915202bf75ca7bd
    
    Mega_email = os.environ.get("Mega_email", "None") # This is not necessary! Enter your mega email only if you have a mega.nz account with pro/business features.
    #If deploying on vps edit the above value as example := Mega_email = "Your-Mega_email-inside-inverted-commas."
    
    Mega_password = os.environ.get("Mega_password", "None") # This is not necessary! Enter your mega password only if you have a mega.nz account with pro/business features.
    #If deploying on vps edit the above value as example := Mega_password = "Your-Mega_password-inside-inverted-commas."
    
    Bot_username = "Pers24_bot"
    
    OWNER_ID = 5114395037
    
    REDIS_URI = "redis-12678.c301.ap-south-1-1.ec2.cloud.redislabs.com:12678"
    
    REDIS_PASS = "GHLdCpHAwBO6e4juHtTcEEsp1OKP2vW0"
    AUTH_USERS = set(int(x) for x in (5273359784, 1031542911))    
    #If deploying on heroku separate the ids by space. (don't put commas. Only separate each of the id's with space)
    
    #If deploying on vps edit the above value as example := 
    #AUTH_USERS = set(int(x) for x in (id1, id2)) 👈 Type exactly as that and replace id1 and id2 with the id's of the telegram users, who you want to allow for multitasking. You cand add many users like that!
    
    DOWNLOAD_LOCATION = "./DOWNLOADS" # The download location for users. (Don't change anything in this field!)
    ADMIN_LOCATION = "./ADOWNLOADS" # The download location for auth users. (Don't change anything in this field!)
    CREDENTIALS_LOCATION = "./CREDENTIALS" # Location where your mega.nz credentials for megatools gets saved if you provide them. (Don't change anything in this field!)
