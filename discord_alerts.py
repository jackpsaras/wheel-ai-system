import requests

def send(webhook, message):
    requests.post(webhook, json={"content": message})