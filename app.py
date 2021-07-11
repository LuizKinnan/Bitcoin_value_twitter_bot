import publisher
import time

api_key = ''
api_secret_key = ''
access_token = ''
access_secret = ''

api = publisher.auth(api_key, api_secret_key, access_token, access_secret)
while True:
    publisher.post(api)
    time.sleep(600)