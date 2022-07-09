import jwt
import base64

# Init our Data
payload = {'school':'udacity'}
algo = 'HS256' #HMAC-SHA 256 HMAC SHA256
secret = 'learning'

encoded_jwt = jwt.encode(payload, secret, algorithm=algo)
print(encoded_jwt)

decoded_jwt = jwt.decode(encoded_jwt, secret, algorithms=algo, verify=True)
print(decoded_jwt)