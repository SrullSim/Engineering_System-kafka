from processes.persister.send_data_to_mongodb import PushToMongodb

tweets_antisemitic = "tweets_antisemitic"
tweets_not_antisemitic = "tweets_not_antisemitic"
host = "localhost"
port = 27017
db_name = "engeneering_system_kafka"
antisemitic_coll = "Antisemitic"
not_antisemitic_coll = "Not_antisemitic"


# PushToMongodb(tweets_antisemitic, host, port, db_name, antisemitic_coll).push()
#
# PushToMongodb(tweets_not_antisemitic, host, port, db_name, not_antisemitic_coll).push()