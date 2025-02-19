import requests


def get_ip(proxy: str) -> (str, bool):
    if proxy and not proxy.startswith('http://'):
        proxy = f'http://{proxy}'
    proxies = {
        "http": proxy,
        "https": proxy,
    } if proxy else None
    try:
        response = requests.get('https://api.ipify.org?format=json', proxies=proxies)
        ip_info = response.json()
        return ip_info['ip']
    except:
        return False
def send_to_telegram(message: str, token, chat_id):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    try:
        requests.post(url, data=payload)
        return True
    except:
        return False