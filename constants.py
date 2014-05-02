def init():
    fin    = open("conf","r")
    line   = fin.read()
    fin.close()
    if line:
        return int(line.split()[0]), line.split()[1]
    return 0, None

def save_config(doc_id, _id):
	fout = open("conf", "w")
	fout.write("%s %s"% (doc_id, _id))

Access_token        = "171007935-2P970TAIQYIdS4lxqp8x6ZzX58eHMc2blmBwLoA7"
Access_token_secret = "uSDbw9JMJIECHlD5WLeymCwaiP99pnzu8XkfxJJ4GHwRk"
CONSUMER_KEY        = "FphPZ38AD3wHRfL7JjxHyQ"
CONSUMER_SECRET     = "FfGDAXDiEdupjn2Bmy9rS1byCAj2gAVzeLB5b6LOo"

mongo_database = "twitter"
mongo_collection = "tweets"
mongo_host = "localhost"
mongo_port = 27017
search_query = 'jobs in lahore'
base_dir = "/home/haider/Development/JobSearch/Search-Engine/data/"
log_file = "/home/haider/Development/JobSearch/Search-Engine/log/log.out"
logger = "myapp"