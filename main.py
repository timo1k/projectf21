import discord

from requests import Session
import json
from discord.ext import tasks



from keep_alive import keep_alive 


client = discord.Client()
#call to the api of coinmarket cap to get the data
#dont need botoom func 
def getETHdata():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
    'symbol':'ETH',
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '', #insert your own api KEY 
    }

    session = Session()
    session.headers.update(headers)
    
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    return data 

def getETHprice():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
    'symbol':'ETH',
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '', #insert your own api KEY 
    }

    session = Session()
    session.headers.update(headers)
    
    response = session.get(url, params=parameters)
    data = json.loads(response.text)

    active_price = data["data"]["ETH"]["quote"]["USD"]["price"]
    active_price = "{0:.2f}".format(active_price)
    return str(active_price)
  
def getsolprice():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
    'symbol':'SOL',
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '', #insert your own api KEY 
    }

    session = Session()
    session.headers.update(headers)
    
    response = session.get(url, params=parameters)
    data = json.loads(response.text)

    active_price = data["data"]["SOL"]["quote"]["USD"]["price"]
    active_price = "{0:.2f}".format(active_price)
    return str(active_price)

def getETHmkc():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
    'symbol':'ETH',
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '', #insert your own api KEY 
    }

    session = Session()
    session.headers.update(headers)
    
    response = session.get(url, params=parameters)
    data = json.loads(response.text)

    mkc = data["data"]["ETH"]["quote"]["USD"]["market_cap"]
    return str(mkc)
  
def getsolmkc():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
    'symbol':'SOL',
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '', #insert your own api KEY  
    }

    session = Session()
    session.headers.update(headers)
    
    response = session.get(url, params=parameters)
    data = json.loads(response.text)

    mkc = data["data"]["SOL"]["quote"]["USD"]["market_cap"]
    return str(mkc)

def getETHrank():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
    'symbol':'ETH',
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '', #insert your own api KEY  
    }

    session = Session()
    session.headers.update(headers)
    
    response = session.get(url, params=parameters)
    data = json.loads(response.text)

    rank = data["data"]["ETH"]["cmc_rank"]
    return str(rank)

def getsolrank():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
    'symbol':'SOL',
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '', #insert your own api KEY 
    }

    session = Session()
    session.headers.update(headers)
    
    response = session.get(url, params=parameters)
    data = json.loads(response.text)

    rank = data["data"]["SOL"]["cmc_rank"]
    return str(rank)

#tells if bot is live on the terminal
@client.event
async def on_ready():
  updateBot.start()
  print('We have logged in as {0.user}'.format(client))
@tasks.loop(seconds = 600)

async def updateBot():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=("PRICE $"+getETHprice())))

#if statements to check the user inputs
@client.event
async def on_message(message):
    #do nothing if the message is from the bot
    if message.author == client.user:
        return
    
    if message.content.startswith('$help'):
        await message.channel.send('Commands:\n$ETH\n$priceETH\n$priceSOL')
        
    if message.content.startswith('$ETH'):
        await message.channel.send('https://coinmarketcap.com/currencies/ethereum/') 
    #embed data which displays coins market cp and live price etc...
    
    if message.content.startswith('$priceETH'):
        embedVar = discord.Embed(title="LIVE PRICE: (ETH)", description= ("$"+(getETHprice())), color=0x9797FF)
        embedVar.add_field(name="Marketcap", value=("$"+getETHmkc()), inline=True)
        embedVar.add_field(name="Rank", value=getETHrank(), inline=True)
        embedVar.set_footer(text="Data From CoinMarketCap")
        await message.channel.send(embed=embedVar)
      
    if message.content.startswith('$priceSOL'):
        embedVar = discord.Embed(title="LIVE PRICE: (SOL)", description= ("$"+(getsolprice())), color=0x9797FF)
        embedVar.add_field(name="Marketcap", value=("$"+getsolmkc()), inline=True)
        embedVar.add_field(name="Rank", value=getsolrank(), inline=True)
        embedVar.set_footer(text="Data From CoinMarketCap")
        await message.channel.send(embed=embedVar)

      
keep_alive()
client.run('') #insert your own discord bot token
