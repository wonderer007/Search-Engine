from pymongo import MongoClient
import json


class MongoDB:
	"""A wrapper class for MongoDB queries"""

	def __init__(self, host, port, database=None, collection=None):
		self.host 	= host
		self.port 	= port
		self.client = MongoClient(self.host, self.port)

		if database is not None:
			self.db = self.client[database]
		if collection is not None:
			self.collection = self.client[collection]

	def collection(self, collection):
		self.collection = self.client[collection]

	def database(self, database):
		self.db = self.client[database]

"""
mongo = MongoDB("localhost", 27017, "test_database", "test_collection")
posts = mongo.db.posts

list = []

list.append( {u'url': u'http://t.co/sh6duSE2wT', u'indices': [70, 92], u'expanded_url': u'http://fb.me/2cl7j1sJc', u'display_url': u'fb.me/2cl7j1sJc'})
list.append( {u'url': u'http://t.co/sh6duSE2wT', u'indices': [70, 92], u'expanded_url': u'http://fb.me/2cl7j1sJc', u'display_url': u'fb.me/2cl7j1sJc'})
list.append( {u'url': u'http://t.co/BGUg9jsMM7', u'indices': [66, 88], u'expanded_url': u'http://lnkd.in/bcvdcza', u'display_url': u'lnkd.in/bcvdcza'})
list.append( {u'url': u'http://t.co/BGUg9jsMM7', u'indices': [66, 88], u'expanded_url': u'http://lnkd.in/bcvdcza', u'display_url': u'lnkd.in/bcvdcza'})
list.append( {u'url': u'http://t.co/Adl28YUjba', u'indices': [80, 102], u'expanded_url': u'http://fb.me/1kXbMaWqF', u'display_url': u'fb.me/1kXbMaWqF'})
list.append( {u'url': u'http://t.co/Adl28YUjba', u'indices': [80, 102], u'expanded_url': u'http://fb.me/1kXbMaWqF', u'display_url': u'fb.me/1kXbMaWqF'})
list.append( {u'url': u'http://t.co/ZSK56uVWHX', u'indices': [60, 82], u'expanded_url': u'http://dlvr.it/5TgcdN', u'display_url': u'dlvr.it/5TgcdN'})
list.append( {u'url': u'http://t.co/ZSK56uVWHX', u'indices': [60, 82], u'expanded_url': u'http://dlvr.it/5TgcdN', u'display_url': u'dlvr.it/5TgcdN'})
list.append( {u'url': u'http://t.co/WFSpwo1D6G', u'indices': [77, 99], u'expanded_url': u'http://dlvr.it/5TgccR', u'display_url': u'dlvr.it/5TgccR'})
list.append( {u'url': u'http://t.co/WFSpwo1D6G', u'indices': [77, 99], u'expanded_url': u'http://dlvr.it/5TgccR', u'display_url': u'dlvr.it/5TgccR'})
list.append( {u'url': u'http://t.co/apcm0zHETS', u'indices': [77, 99], u'expanded_url': u'http://fb.me/3ThKyr0QR', u'display_url': u'fb.me/3ThKyr0QR'})
list.append( {u'url': u'http://t.co/apcm0zHETS', u'indices': [77, 99], u'expanded_url': u'http://fb.me/3ThKyr0QR', u'display_url': u'fb.me/3ThKyr0QR'})
list.append( {u'url': u'http://t.co/DM6Cc134vE', u'indices': [117, 139], u'expanded_url': u'http://fb.me/2W06YXUk7', u'display_url': u'fb.me/2W06YXUk7'})
list.append( {u'url': u'http://t.co/DM6Cc134vE', u'indices': [117, 139], u'expanded_url': u'http://fb.me/2W06YXUk7', u'display_url': u'fb.me/2W06YXUk7'})

for item in list:
	post_id = posts.insert(item)
	print post_id
"""