from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "23801623"))
    API_HASH = getenv("API_HASH", "fb68765576f27849a3de745d1fe81b74")
    BOT_TOKEN = getenv("BOT_TOKEN", "6729293205:AAH1GidKTd_QuaseX7hQw9rSQlU5HnF_j5A")
    CHID = int(getenv("CHID", "-1002029565703"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://tamil:tamil@2003@cluster0.svg2af2.mongodb.net/")
    LOGCHID = int(getenv("LOGCHID", "-1002029565703"))
    API = getenv("API", "abcdefu67-8dgdg")
cfg = Config()
