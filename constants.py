def get_cities():
    fin    = open("cities.txt","r")
    cities = []
    for city in fin:
    	cities.append(city)
    return cities


Access_token        = "your-access-token"
Access_token_secret = "your access secret"
CONSUMER_KEY        = "your consumer key"
CONSUMER_SECRET     = "your consumer secret"

mongo_database = "twitter"
mongo_collection = "tweets"
mongo_host = "localhost"
mongo_port = 27017
search_query = 'jobs in lahore'
base_dir = "/root/Development/Search-Engine/data/"
log_file = "/root/Development/Search-Engine/log/log.out"
logger = "myapp"
