import requests
import json
# Save the cookies to reuse


def save_session(session):
    with open('cookies/cookies.txt', 'w') as f:
        json.dump(requests.utils.dict_from_cookiejar(session.cookies), f)

# Load cookies


def load_sesion(session):
    with open('cookies/cookies.txt', 'r') as f:
        session.cookies = requests.utils.cookiejar_from_dict(json.load(f))
