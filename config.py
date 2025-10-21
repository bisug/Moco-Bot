from os import getenv
import os

from dotenv import load_dotenv
load_dotenv()

API_ID = int(getenv("API_ID", None))
API_HASH = getenv("API_HASH", None)
BOT_TOKEN = getenv("BOT_TOKEN", None)

OWNER_ID = int(getenv("OWNER_ID", 7804972365))

MONGO_URL = getenv("MONGO_URL", None)

WEB_APP = getenv("WEB_APP", False) 

LOGGER_GROUP_ID = int(getenv("LOGGER_GROUP_ID", None))

BOT_NAME = os.environ.get("BOT_NAME",None)
BOT_USERNAME = os.environ.get("BOT_USERNAME", None)

SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "SuMelodyVibes")
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "dear_sumi")


LIKE_API_URL = os.environ.get("LIKE_API_URL", "http://69.62.118.156:19126")
LIKE_API_KEY = os.environ.get("LIKE_API_KEY", "freeapi")

STICKER = [
"CAACAgUAAxkBAAEE9_hoGsRQ0QGcSTsVoL3yGE9H6uL9DQACKBMAAiCuIFfJhh9sfRPfTh4E",
"CAACAgUAAxkBAAEE9_toGsR2hVeHYvTmHBgWPqVZwmTOVQACBRkAAlStIFdUJrsjwSkhVR4E",
"CAACAgUAAxkBAAEE9_9oGsTV5Por2uHhoXsm5GB6-UEWLQACGRQAAuxN6FYUY25_DI9rjh4E",
"CAACAgUAAxkBAAEE9_5oGsSYHBAwbkaebVeuVr5mTVRyBwACFBMAAhg8wVUUKEUeTc3kSR4E",
"CAACAgUAAxkBAAJSVmhPs5Z_YYIUc5HuXS5VOik1NdBxAAK1GwACDav4VWKwXqHw154LHgQ", 
"CAACAgUAAxkBAAJSWWhPs7_7oWTnXWnJSJ-8NzJ_kGoHAAKHEgACUZV5V7didh8P5BaRHgQ", 
"CAACAgUAAxkBAAJSXmhPs-5T1YL2iNbDiaS9PqpzBYRyAAKkFQACgeyoV8w7WaAGY90OHgQ", 
"CAACAgUAAxkBAAJSXWhPs-fjxka6HacJk6ateGQRoAIGAAL2EwACyU6oV1Pre1yG6uiRHgQ", 
"CAACAgUAAxkBAAJSXGhPs91YiR3Wi8Oy0TuQgb-x0RiAAAKpGAAC-F-oV9VRQNmH_F3THgQ", 
]


IMG = [
"https://i.ibb.co/4wZD3q8x/ed7f8d606863.jpg",
"https://i.ibb.co/4wZD3q8x/ed7f8d606863.jpg",
"https://i.ibb.co/4wZD3q8x/ed7f8d606863.jpg", 
"https://i.ibb.co/B26dnCz6/7b1fbeac153b.jpg", 
]
