from pymongo import MongoClient
import json


class MongoDB:
	"""A wrapper class for MongoDB queries"""

	def __init__(self, host="localhost", port=27017, database=None, collection=None):
		self.host = host
		self.port = port
		self.client = MongoClient(self.host, self.port)

		if database and collection:
			self.db = self.client[database]
			self.collection = self.db[collection]

	def insert(self, json_obj):
		self.collection.insert(json_obj)