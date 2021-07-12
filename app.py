import publisher
import time

api_key = '[YOUR API KEY]'
api_secret_key = '[YOUR SECRET API KEY]'
access_token = '[YOUR TOKEN]'
access_secret = '[YOU TOKEN]'

api = publisher.auth(api_key, api_secret_key, access_token, access_secret)
while True:
    publisher.post(api)
    time.sleep(600)