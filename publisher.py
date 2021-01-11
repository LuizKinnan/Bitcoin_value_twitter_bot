import twitter
import req

def login(key, secret_key, access_token, access_token_secret):

    return twitter.Api(consumer_key=key,
            consumer_secret=secret_key,
            access_token_key=access_token,
            access_token_secret=access_token_secret)

def post(api):
    
    result = req.consult()
    #print(f'Nesse momento 1 Bitcoin está valendo {result}')
    try:
        status = api.PostUpdate(f'Nesse momento 1 Bitcoin está valendo {result}.')
    except:
        print('Duplicada')
