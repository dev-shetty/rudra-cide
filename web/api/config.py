import os
from dotenv import load_dotenv
load_dotenv()

KEY = os.getenv('KEY')

# Redis 
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')
REDIS_DB = os.getenv('REDIS_DB')

# Reddit
REDDIT_API_CLIENT = os.getenv('REDDIT_API_CLIENT')
REDDIT_API_SECRET = os.getenv('REDDIT_API_SECRET')

OPEN_API_KEY = os.getenv('OPEN_API_KEY')