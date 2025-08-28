from loader import Loader
from config.config import URI
from config.config import DB_NAME

uri = URI
db_name = DB_NAME
Loader(uri, db_name).pull_massages_by_time(
    "CreateDate",
    {1: "raw_tweets_antisemitic",0: "raw_tweets_not_antisemitic"}
    ,"Antisemitic")