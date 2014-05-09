def get_cities():
    fin    = open("cities.txt","r")
    cities = []
    for city in fin:
    	cities.append(city)
    return cities


Access_token        = "171007935-2P970TAIQYIdS4lxqp8x6ZzX58eHMc2blmBwLoA7"
Access_token_secret = "uSDbw9JMJIECHlD5WLeymCwaiP99pnzu8XkfxJJ4GHwRk"
CONSUMER_KEY        = "FphPZ38AD3wHRfL7JjxHyQ"
CONSUMER_SECRET     = "FfGDAXDiEdupjn2Bmy9rS1byCAj2gAVzeLB5b6LOo"

mongo_database = "twitter"
mongo_collection = "tweets"
mongo_host = "localhost"
mongo_port = 27017
search_query = 'jobs in lahore'
base_dir = "/root/Development/Search-Engine/data/"
log_file = "/root/Development/Search-Engine/log/log.out"
logger = "myapp"
