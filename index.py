from bs4 import BeautifulSoup
from constants import *
from TwitterAPI import TwitterAPI
from scrap import Scraper
import time
import logging
import json
import urllib2



# get logging handler
logger = logging.getLogger(logger)
hdlr = logging.FileHandler(log_file)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)

count , max_id = init()

for x in range(2):
    if x%5 is 0:
        api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, Access_token, Access_token_secret)

    json_str = {}
    json_str['q'] = search_query
    json_str['count'] = "100"
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
            item['ser_id'] = count
            count +=1
            thread = Scraper(item['entities']['urls'][0]['expanded_url'], item)
            thread.start()
            if count%5 is 0:
                save_config(count, max_id)

    time.sleep(3)