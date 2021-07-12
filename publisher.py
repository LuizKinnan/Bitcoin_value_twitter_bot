import twitter
import req

def auth(api_key, api_secret_key, access_token, access_secret):
    api = twitter.Api(consumer_key=api_key, consumer_secret=api_secret_key, access_token_key=access_token, access_token_secret=access_secret)
    
    return api

def post(api):
    
    result = req.consult()
    try:
        status = api.PostUpdate(f'Nesse momento 1 Bitcoin está valendo {result}.')
    except:
        print('Duplicada, não publicada')
