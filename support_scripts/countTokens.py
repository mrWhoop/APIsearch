import tiktoken
from app.extensions import mongo

def countGPTtokens():
    encoding = tiktoken.encoding_for_model("text-embedding-ada-002")
    apis = mongo.db.apis.find()
    tokens = 0
    for api in apis:
        token = encoding.encode(api['description'])
        tokens += len(token)
        if 8191 < len(token):
            return 'Some are too long for ada2'

    return tokens