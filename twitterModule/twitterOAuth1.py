from requests_oauthlib import OAuth1
from os.path import dirname, abspath
from os import getenv
from dotenv import load_dotenv


def oath():
    baseDir = dirname(abspath(__file__))

    load_dotenv(verbose=True)
    load_dotenv(f"{baseDir}/.env_s")

    CONSUMER_KEY = getenv("TWITTER_API_KEY")
    CONSUMER_SECRET = getenv("TWITTER_API_SECRET")
    ACCESS_TOKEN = getenv("TWITTER_ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = getenv("TWITTER_ACCESS_TOKEN_SECRET")

    oauth = OAuth1(
        CONSUMER_KEY,
        client_secret=CONSUMER_SECRET,
        resource_owner_key=ACCESS_TOKEN,
        resource_owner_secret=ACCESS_TOKEN_SECRET,
    )

    return oauth
