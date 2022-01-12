import requests
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook

url = 'https://www.bbc.com/news'
response = requests.get(url)
  
soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find('body').find_all('h3')
unwanted = ['BBC World News TV', 'BBC World Service Radio',
            'News daily newsletter', 'Mobile app', 'Get in touch']
  
for x in list(dict.fromkeys(headlines)):
    if x.text.strip() not in unwanted:
        webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/930888946110595122/MLFyDeDhcD7o3hOFakr5YCwaBBpZhD0dI2vjekqguRine_8L12uH7RNdUWywzBrkUpnL', rate_limit_retry=True,
                            content=f'{x.text.strip()}')
        response = webhook.execute()
        print(x.text.strip())