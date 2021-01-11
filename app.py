import publisher
import time

key = '[YOUR API KEY]'
secret_key = '[YOUR SECRET API KEY]'
token = '[YOUR TOKEN]'
secret_token = '[YOUR SECRET TOKEN]'

api = poster.login(key, secret_key, token, secret_token)
while True:
    poster.post(api)
    time.sleep(600)
