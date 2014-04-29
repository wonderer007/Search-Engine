from bs4 import BeautifulSoup
from constants import *
from TwitterAPI import TwitterAPI
from scrap import Scraper
import time
import json
import urllib2

#api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, Access_token, Access_token_secret)
count , max_id = init()
count

for x in range(30):
    if x%5 is 0:
        api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, Access_token, Access_token_secret)

    if x%15 is 0:
        save_config(count, max_id)

    json_str = {}
    json_str['q'] = search_query
    json_str['count'] = "50"
    if max_id is not None:
    	json_str['max_id'] = max_id

    try:
        r = api.request('search/tweets', json_str)
    except:
        pass
    for item in r.get_iterator():
        max_id = item['id']
        if item['entities']['urls']:
            max_id = item['id']
            item['doc_id'] = count
            count +=1
            thread = Scraper(count, item['entities']['urls'][0]['expanded_url'], item)
            thread.start()

    time.sleep(3)