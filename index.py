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

count =0
cities = get_cities()
api = None

for city in cities:
    print city
    print "-------------"

    tmp_count =0
    max_id = None
    finish = False
    while not finish:
        if api is None:
            api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, Access_token, Access_token_secret)

        tmp_count +=1
        json_str = {}
        json_str['q'] = "%s %s" % ("jobs", city)
        json_str['count'] = "2"

        if max_id is not None:
        	json_str['max_id'] = max_id
        
        try:
            r = api.request('search/tweets', json_str)
            response = json.loads(r.response.text)
        except:
            pass

        for tweet in response['statuses']:
            max_id = tweet['id']
            if tweet['entities']['urls']:
                max_id = tweet['id']
                tweet['ser_id'] = count
                count +=1
                thread = Scraper(tweet['entities']['urls'][0]['expanded_url'], tweet)
                thread.start()
        
        if not response['statuses'] or tmp_count is 2:
            finish = True