import os
from dotenv import load_dotenv
load_dotenv()


DEBUG = True
API_KEY = os.environ.get('API_KEY')
CACHE_TYPE = 'SimpleCache'
CACHE_DEFAULT_TIMEOUT = 300
