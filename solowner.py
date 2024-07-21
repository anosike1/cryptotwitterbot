import tweepy
import requests
import schedule
import time

# Twitter API credentials
API_KEY = *insert yours here*
API_SECRET_KEY = *insert yours here*
ACCESS_TOKEN = *insert yours here*
ACCESS_TOKEN_SECRET = *insert yours here*
BEARER_TOKEN = *insert yours here*

# Set up tweepy authentication
client = tweepy.Client (
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
    wait_on_rate_limit=True
    )

def get_price(coin_id = 'solana'):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data[coin_id]['usd']

def update_status():
    crypto_price = get_price()
    status = f"The current price of $SOL is ${crypto_price:.2f}. #Solana #Crypto"
    client.create_tweet (text=status)
    print("Tweeted:", status)

# Schedule the bot to run every 8 hours
schedule.every(8).hours.do(update_status)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1) 
