from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "01122344"))
    API_HASH = getenv("API_HASH", "abcdefg")
    BOT_TOKEN = getenv("BOT_TOKEN", "1234567891:AdDfgFRFVVfDEhdhyjjvjjftSEW")

config = Config()
