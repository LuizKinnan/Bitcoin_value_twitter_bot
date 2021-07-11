import requests
from bs4 import BeautifulSoup as bs

def consult():

    response = requests.get('https://www.google.com/search?sxsrf=ALeKk037KvgJf7RElKMc_Ph38wZNSdUKCQ%3A1610387920684&ei=0JH8X6qXKY685OUPwtyjgAU&q=bitcoin&oq=bitcoin&gs_lcp=CgZwc3ktYWIQAzIJCCMQJxBGEIICMgQIIxAnMgQIIxAnMggIABCxAxCDATIKCAAQsQMQgwEQQzIKCAAQsQMQgwEQQzIICAAQsQMQgwEyCAgAELEDEIMBMgoIABCxAxCDARBDMggIABCxAxCDAToECAAQRzoECAAQQzoCCAA6BggAEBYQHjoFCAAQsQM6BQguELEDOgIILjoHCCMQ6gIQJzoJCCMQ6gIQJxATOggILhCxAxCDAToICAAQxwEQrwFQ3KAxWKSwMWC0sTFoAXADeACAAZIBiAHqCJIBAzAuOZgBAKABAaoBB2d3cy13aXqwAQrIAQfAAQE&sclient=psy-ab&ved=0ahUKEwiqv9m_upTuAhUOHrkGHULuCFAQ4dUDCA0&uact=5')    
    content = bs(response.text, 'html5lib')
    block = content.find_all("div", {"class":"BNeawe iBp4i AP7Wnd"})
    value = block[1].text
    return block[1].text