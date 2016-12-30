import requests
import datetime
from bs4 import BeautifulSoup
import twitter_tokens as tw
from requests_oauthlib import OAuth1Session
import hatena_auth as hatena

# auth info
USER = hatena.USER
APIKEY = hatena.APIKEY
URL = hatena.URL
REPEAT = hatena.REPEAT

session = requests.session()
twitter = None

def main():
    drafts = get_drafts()
    reserve = get_reserve(drafts)
    text = tweet_extract(reserve)
    token_init()
    print(tweet(text))

def get_drafts():
    drafts = []
    global URL
    
    for i in range(REPEAT):
        res = session.get(URL,auth=(USER,APIKEY))
        soup = BeautifulSoup(res.text, "html.parser")
        URL = soup.find("link", rel="next").get('href')

        article = soup.find("feed").find_all("entry")
        for art in article:
            isdraft = art.find("app:control").find("app:draft").text
            if isdraft == 'yes':
                title = art.find("title").text
                updated = art.find("updated").text
                draft=[title,updated]
                drafts.append(draft)
    return drafts

def get_reserve(drafts):
    reserve = []
    now = datetime.datetime.now()

    for draft in drafts:
        date = datetime.datetime.strptime(draft[1],"%Y-%m-%dT%H:%M:%S+09:00")
        if now < date:
            #convert string to datetime
            draft[1] = date
            reserve.append(draft)
    return reserve

def tweet_extract(reserve):
    text = "update notice:"
    for art in reserve:
        date = art[1].strftime('%m/%d')
        
        if len(text) + len(art[0]) > 140:
            break
        text += "%s:%s" % (date,art[0])
    return text

def token_init():
    consumer_key = tw.tokens['consumer_key']
    consumer_secret = tw.tokens['consumer_secret_key']
    access_key = tw.tokens['access_token_key']
    access_secret  = tw.tokens['access_token_secret_key']

    global twitter
    twitter = OAuth1Session(consumer_key, consumer_secret, access_key, access_secret)

def tweet(text):
    URL = 'https://api.twitter.com/1.1/statuses/update.json'

    payload = {'status': text}
    req = twitter.post(URL, params = payload)

    return req.status_code

if __name__ == '__main__':
    main()

