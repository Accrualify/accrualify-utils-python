# Uses python3
# pip3 install requests

from hashlib import sha256
import hmac, time
import requests
import codecs

svb_api_key = ''  # Set the token here
svb_sec_key = ''  # Set the HMAC here

secret = svb_sec_key
timestamp = str(int(time.time()))
method = 'GET'
path = '/v1/realcards'
params = ''
body = ''
print(timestamp)
message = "\n".join([timestamp, method, path, params, body])
message = message
signature = hmac.new(codecs.encode(secret), codecs.encode(message), sha256).hexdigest()
print(signature)

headers = {
    'Authorization': 'Bearer ' + svb_api_key,
    'X-Signature': signature,
    'X-Timestamp': timestamp,
    'Accept': 'application/json'
}
response = requests.get(url='https://api.svb.com' + path, headers=headers)

print(response.text)
