# cryptoDataBot
## Needed:
### Discord Bot Token (*insert discord token*), and a api key to CoinMarketCap (*insert api key*)
## functionality
### View the live price (or data like marketcap) of BTC ETH SOL within a group on discord through a bot. Also more features like displaying the live price of any of the crypto assets we choose will be displayed on discord side bar (under the discord bot's name).
### def getETHprice():

### def getETHmkc():

### def getETHrank():

## newest update: cool functionality:
### async def updatewoof():
###  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=("PRICE $"+getETHprice())))
#### updates the discord bot status to show the live price of ETH without any user commands (every 600 seconds to not get rate limited)

#### last update: 9/29/22

