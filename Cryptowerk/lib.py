import requests
import hashlib
from dotenv import load_dotenv
import os 

def getHash(text_path, isFile = True):
    if isFile:
        return getHashFile(text_path)
    hash_object = hashlib.sha256(text.encode() )
    return hash_object.hexdigest()

def getHashFile(path):
    sha256_hash = hashlib.sha256()
    with open(path,"rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def register(hash):
    
    load_dotenv()

    API_KEY = os.getenv('PROJECT_API_KEY')
    SECRET = os.getenv('SECRET')

    headers = {
        'X-ApiKey': API_KEY + ' ' + SECRET
    }

    data = {
        'hashes': hash
    }

    response = requests.post('https://developers.cryptowerk.com/platform/API/v8/register', headers=headers, data=data)
    return response.json()

def verify(response):
    retrievalId = response['documents'][0]['retrievalId']
    load_dotenv()

    API_KEY = os.getenv('PROJECT_API_KEY')
    SECRET = os.getenv('SECRET')

    headers = {
        'X-ApiKey': API_KEY + ' ' + SECRET
    }

    data = {
        'retrievalId': retrievalId
    }

    response = requests.post('https://developers.cryptowerk.com/platform/API/v8/verify', headers=headers, data=data)
    return response.json()

if __name__ == "__main__":
    # hash = getHash("Hello...")
    hash = getHash("C:\\Development\\Personal\\mU-Insurance\\Policy.pdf")
    print(hash)
    register_response = register(hash)

    register_response = {
        'maxSupportedAPIVersion': 8, 
        'documents': [
            {'retrievalId': 'ri3241174c7d7055eaab7f3138c2709a3aece1b1b801c1fd8ddc67ec5f6757e2132'}
        ], 
        'minSupportedAPIVersion': 1
    }

    verify_response = verify(register_response)
    print(verify_response)