from fastapi import FastAPI
from processes.persister import persister_manger
import uvicorn
from dal_mongo.mongo_localhost_dal import MongoDALLocalhost

app = FastAPI()

@app.get("/antisemitic_tweets")
def antisemitic_tweets():
    my_json = MongoDALLocalhost(
        persister_manger.host,
        persister_manger.port,
        persister_manger.db_name,
        persister_manger.antisemitic_coll).get_collection()
    return my_json

@app.get("/not_antisemitic_tweets")
def not_antisemitic_tweets():
    my_json = MongoDALLocalhost(
        persister_manger.host,
        persister_manger.port,
        persister_manger.db_name,
        persister_manger.tweets_not_antisemitic).get_collection()
    return my_json


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port = 8080)