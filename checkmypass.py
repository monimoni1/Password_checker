import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    #print(res)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, Check the API and try again.')
    return res


def pwned_api_check(password):
    sha1password = hashlib.sha1()
request_api_data('123')

#use SHA1 hash generator to generate a hashed password
# use only first five letters of the hash function to create extra layer of protection called K security.