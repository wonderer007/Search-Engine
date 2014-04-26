from bs4 import BeautifulSoup
from mongo import MongoDB
import urllib2
import urllib
import threading
import json

mongo_database = "my_db"
mongo_collection = "tweets"
mongo_host = "localhost"
mongo_port = 27017

class Scraper(threading.Thread):
	base_dir = "/home/haider/Development/JobSearch/data/"
	mongo = MongoDB(mongo_host, mongo_port, mongo_database, mongo_collection)
	tweet = mongo.db.tweets
	urls = {}




	def __init__(self, _id, _url, _json):
		threading.Thread.__init__(self)
		self.url = _url
		self.id = _id
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
			return

		self.urls[self.url] = True
		header = {'User-Agent': 'Mozilla/5.0'}
		req = urllib2.Request(self.url,headers=header)
		page = urllib2.urlopen(req)
		soup = BeautifulSoup(page)

		# kill all script and style elements
		for script in soup(["script", "style", "a"]):
		    script.extract()    # rip it out

		# get text
		text = soup.get_text()

		# break into lines and remove leading and trailing space on each
		lines = (line.strip() for line in text.splitlines())
		# break multi-headlines into a line each
		chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
		# drop blank lines
		text = '\n'.join(chunk for chunk in chunks if chunk)
		fin = open(self.base_dir+ str(self.id), "w")
		self.tweet.insert(self.json)
		print "Tweet inserted in mongo"
		fin.write(text.encode('utf-8'))
		fin.close()

#url = "http://newjobs.pk/government-jobs/medical/jobs-in-shalamar-hospital-lahore"
#thraed = Scraper(1,url)
#thraed.start()