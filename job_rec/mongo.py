from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import requests
uri = "mongodb+srv://arunkumar22112003:welcome123@cluster0.6d2srpa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db=client.jobs
collection=db.naukri

items = collection.find().limit(5)

hf_token = "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"
embedding_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"

def generate_embedding(text):
    response = requests.post(embedding_url, headers={"Authorization": f"Bearer {hf_token}"}, json={"inputs": text})
    if response.status_code == 200:
        return response.json()
    return None

# for doc in collection.find({'Job Title': {'$exists': True}, 'Key Skills': {'$exists': True}}).limit(50):
#     job_title = doc['Job Title']
#     job_description = doc['Key Skills']
#     text = job_title+job_description
#     doc['embedd_id'] = generate_embedding(text)
#     collection.replace_one({'_id': doc['_id']}, doc)

query = "software engineer python java c++"

results = collection.aggregate([
    {
        "$vectorSearch":{
            "queryVector":generate_embedding(query),
            "path":"embedd_id",
            "numCandidates":100,
            "limit":5,
            "index":"embed_index"
        }
    }
])

for document in results:
    print(document['Job Title'], document['Key Skills'], document['Role'], document['Industry'])
    print("=================================================================================")