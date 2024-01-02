import requests
import os

class TelegramNewsSender:
    def __init__(self):
        token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.channel_id = os.getenv('TELEGRAM_CHANNEL_ID')
        self.base_url = f'https://api.telegram.org/bot{token}/'

    def send(self, title, url):
        message_text = f"*{title}*\n\n{url}"

        params = {
            'chat_id': self.channel_id,
            'text': message_text,
            'parse_mode': 'Markdown',
        }

        response = requests.get(self.base_url + 'sendMessage', params=params)
        response.raise_for_status()
