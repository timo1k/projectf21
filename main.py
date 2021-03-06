import discord

from requests import Session
import json




from keep_alive import keep_alive 

client = discord.Client()
#call to the api of coinmarket cap to get the data

def getwoofdata():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
    'symbol':'WOOF',
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'c1b04b2e-baf0-4989-9118-6ccd8ae1e8a6',
    }

    session = Session()
    session.headers.update(headers)
    
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    return data 

def getwoofprice():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
    'symbol':'WOOF',
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'c1b04b2e-baf0-4989-9118-6ccd8ae1e8a6',
    }

    session = Session()
    session.headers.update(headers)
    
    response = session.get(url, params=parameters)
    data = json.loads(response.text)

    active_price = data["data"]["WOOF"]["quote"]["USD"]["price"]
    return str(active_price)

def getwoofmkc():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
    'symbol':'WOOF',
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'c1b04b2e-baf0-4989-9118-6ccd8ae1e8a6',
    }

    session = Session()
    session.headers.update(headers)
    
    response = session.get(url, params=parameters)
    data = json.loads(response.text)

    mkc = data["data"]["WOOF"]["quote"]["USD"]["market_cap"]
    return str(mkc)

def getwoofrank():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
    'symbol':'WOOF',
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'c1b04b2e-baf0-4989-9118-6ccd8ae1e8a6',
    }

    session = Session()
    session.headers.update(headers)
    
    response = session.get(url, params=parameters)
    data = json.loads(response.text)

    rank = data["data"]["WOOF"]["cmc_rank"]
    return str(rank)

#tells if bot is live on the terminal
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#if statements to check the user inputs
@client.event
async def on_message(message):
    #do nothing if the message is from the bot
    if message.author == client.user:
        return
    
    if message.content.startswith('$help'):
        await message.channel.send('Commands:\n$woof\n$live\n$freewoof')
        
    if message.content.startswith('$woof'):
        await message.channel.send('https://coinmarketcap.com/currencies/woof/') 
    #embed data which displays coins market cp and live price etc...
    
    if message.content.startswith('$live'):
        embedVar = discord.Embed(title="LIVE PRICE", description= ("$"+getwoofprice()), color=0x9797FF)
        embedVar.add_field(name="Marketcap", value=("$"+getwoofmkc()), inline=True)
        embedVar.add_field(name="Rank", value=getwoofrank(), inline=True)
        embedVar.set_footer(text="Data From CoinMarketCap")
        await message.channel.send(embed=embedVar)

    if message.content.startswith('$freewoof'):
        await message.channel.send('https://media.giphy.com/media/Ju7l5y9osyymQ/giphy.gif')






      
keep_alive()
client.run('OTExNDc4NTQ2MTMwNjg1OTgz.YZh-iw.rKoyRGoAtHDvS1rfANiVKG8I34Y')
