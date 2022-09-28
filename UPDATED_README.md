# cryptoDataBot
## Needed:
### Discord Bot Token (*insert discord token*), and a api key to CoinMarketCap (*insert api key*)
## functionality
### View the live price (or data like marketcap) of BTC ETH SOL within a group on discord through a bot. Also more features like displaying the live price of any of the crypto assets we choose will be displayed on discord side bar (under the discord bot's name).
### def getETHprice():

### def getETHmkc():

### def getETHrank():

## cool functionality:
### @tasks.loop(seconds = 600)
### async def updatewoof():
###  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=("PRICE $"+getETHprice())))
  


# tools used:
## https://www.youtube.com/watch?v=t75nMHEuU2I https://www.youtube.com/watch?v=Wd26AIfgTpA https://www.geeksforgeeks.org/convert-json-to-dictionary-in-python/ https://jsonformatter.curiousconcept.com/# https://coinmarketcap.com/api/documentation/v1/#section/Introduction
### These were used to help navigate the api with python and get the specific data we needed
## https://realpython.com/how-to-make-a-discord-bot-python/ https://www.youtube.com/watch?v=SPTfmiYiuok https://uptimerobot.com/dashboard#789894739 https://replit.com/@timo1k/UnsungFearlessCleaninstall#main.py 
### These were used to help get the bot up and running 24/7
## https://discordpy.readthedocs.io/en/stable/api.html
### used for overall help, like how to create embed messages
