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
fopen = open("log/output.txt","w")


for city in cities:
    print city
    print "-------------"
    fopen.write(city+"\n")


    max_id = None
    finish = False
    while not finish:
        pre_count = Scraper.count
        if api is None:
            api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, Access_token, Access_token_secret)


        json_str = {}
        json_str['q'] = "%s %s" % ("jobs", city)
        json_str['count'] = "100"

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
                fopen.write(tweet['text'].encode('utf-8') +"\n")
                fopen.write(str(count) + "\n")
                fopen.write("--------" + "\n")
                thread = Scraper(tweet['entities']['urls'][0]['expanded_url'], tweet)
                thread.start()
        
        if not response['statuses']:
            finish = True

        if pre_count is Scraper.count:
            finish = True
        time.sleep(3)


fopen.write("File Closed")
fopen.close()
