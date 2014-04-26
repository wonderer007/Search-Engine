import json
import urllib2
from bs4 import BeautifulSoup
from TwitterAPI import TwitterAPI
from scrap import Scraper
import time


Access_token        = "171007935-2P970TAIQYIdS4lxqp8x6ZzX58eHMc2blmBwLoA7"
Access_token_secret = "uSDbw9JMJIECHlD5WLeymCwaiP99pnzu8XkfxJJ4GHwRk"
CONSUMER_KEY        = "FphPZ38AD3wHRfL7JjxHyQ"
CONSUMER_SECRET     = "FfGDAXDiEdupjn2Bmy9rS1byCAj2gAVzeLB5b6LOo"
TRACK_TERM = 'jobs in lahore'
api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, Access_token, Access_token_secret)
count =0
max_id = None


for x in range(30):
    if x%5 is 0:
        api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, Access_token, Access_token_secret)

    json_str = {}
    json_str['q'] = "Jobs in Lahore"
    json_str['count'] = "2"
    if max_id is not None:
    	json_str['max_id'] = max_id

    r = api.request('search/tweets', json_str)
    for item in r.get_iterator():
        max_id = item['id']
        if item['entities']['urls']:
            max_id = item['id']
            item['doc_id'] = count
            count +=1
            thread = Scraper(count, item['entities']['urls'][0]['expanded_url'], item)
            thread.start()

    time.sleep(3)
