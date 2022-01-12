# NEWS-DAILY

Python application to generate news at a particular time using python.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install -r requirements.txt.

```bash
pip install -r requirements.txt
```

## Usage

```python
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
        webhook = DiscordWebhook(url='#yourwebhook', rate_limit_retry=True,
                            content=f'{x.text.strip()}')
        response = webhook.execute()
        print(x.text.strip())
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Brokiemag](https://brokiemag.me)
