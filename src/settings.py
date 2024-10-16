import os

from loadotenv import load_env

load_env()

DB_URI = os.getenv('DB_URI')
RIOT_API = os.getenv('RIOT_API')
