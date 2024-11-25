import requests

def send_message(text):
    url = f"https://api.telegram.org/bot7372580855:AAFFiQMTgiCbxW9xI-Vy5IEW9IAJGzUc8bk/sendMessage"
    params = {"chat_id": '7478200510', "text": text}
    response = requests.post(url, data=params)
    return response.json()