from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from reddit_posts import content_dict

uri = 'mongodb+srv://vaidyameet2004:C3Gs6N5JeW4CbJXo@cluster0.zhfq3eq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

    db = client['reddit_db']
    stories = db.stories

    for post_id, post_info in content_dict.items():
        # Add the Reddit post ID to the post info
        post_info['_id'] = post_id

        # Insert the post info into the MongoDB collection
        stories.insert_one(post_info)
    

except Exception as e:
    print(e)