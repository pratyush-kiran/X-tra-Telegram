import requests

headers = {
    'Content-Type': 'application/json',
}

data = '{"chat_id":"@x64_bits", "text":"Testing", "reply_markup": {"inline_keyboard": [[{"text":"Visit Unofficed", "url": "http://unofficed.com"}]]} }'

response = requests.post('https://api.telegram.org/bot$apiToken/sendMessage', headers=headers, data=data)
