import environ

env = environ.Env()
environ.Env.read_env()

API_KEY = env('API_KEY')
API_KEY_SECRET = env('API_KEY_SECRET')

ACCESS_TOKEN = env('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = env('ACCESS_TOKEN_SECRET')