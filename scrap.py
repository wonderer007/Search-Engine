from bs4 import BeautifulSoup
from mongo import MongoDB
from constants import *
import logging
import urllib2
import urllib
import threading
import json


# get logging handler
logger = logging.getLogger(logger)
hdlr = logging.FileHandler(log_file)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)

class Scraper(threading.Thread):

	logger.info("Connecting with mongo database with parameters .....")
	logger.info("host %s" %(mongo_host))
	logger.info("port %s" %(mongo_port))
	logger.info("database %s" %(mongo_database))

	mongo = MongoDB(mongo_host, mongo_port, mongo_database, mongo_collection)
	tweet = mongo.db.tweets
	urls = {}
	count =1


	def __init__(self, _url, _json):
		threading.Thread.__init__(self)
		self.url = _url
		self.json = _json
		try:
			resp = urllib.urlopen(self.url)
		except:
			return
		if resp.getcode() is 200:
			self.url = resp.url

	def run(self):
	
		if self.urls.has_key(self.url):
			print "URL %s has already been visited " % (self.url)
			logger.info("URL %s has already been visited " % (self.url))
			return

		self.urls[self.url] = True
		header = {'User-Agent': 'Mozilla/5.0'}
		req = urllib2.Request(self.url,headers=header)
		try:
			logger.info("Making HTTP request for url %s " % (self.url))
			page = urllib2.urlopen(req)
		except:
			logger.info("HTTP request for url %s is crashed" % (self.url))
			return

		logger.info("HTTP Request for url %s successfull" % (self.url))
		soup = BeautifulSoup(page)

		# kill all script and style elements
		for script in soup(["script", "style", "a"]):
		    script.extract()    # rip it out

		# get text
		text = soup.get_text()

		# break into lines and remove leading and trailing space on each
		lines 	= (line.strip() for line in text.splitlines())
		# break multi-headlines into a line each
		chunks 	= (phrase.strip() for line in lines for phrase in line.split("  "))
		# drop blank lines
		text 	= '\n'.join(chunk for chunk in chunks if chunk)
		fin 	= open(base_dir+ str(Scraper.count), "w")
		print Scraper.count
		self.json['doc_id'] = Scraper.count
		Scraper.count +=1
		self.tweet.insert(self.json)
		print "Tweet inserted in mongo"
		logger.info("Tweet inserted in mongo")
		fin.write(text.encode('utf-8'))
		fin.close()

#url = "http://newjobs.pk/government-jobs/medical/jobs-in-shalamar-hospital-lahore"
#thraed = Scraper(1,url)
#thraed.start()