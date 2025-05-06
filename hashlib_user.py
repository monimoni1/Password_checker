import hashlib
import requests
# Declaring Password
# adding 5gz as password
#salt = "5gz"
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    #print(res)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, Check the API and try again.')
    return res

def read_res(response):
    print(response.text)
# Adding salt at the last of the password
#dataBase_password = password #+ salt
# Encoding the password
def pwned_api_check(hashed):
    hashed_sha1 = hashlib.sha1(hashed.encode('utf-8')).hexdigest().upper()
    first_five, tail = hashed_sha1[:5], hashed_sha1[5:]
    request_api_data(first_five)
    print(response)
    return read_res(response)

# Printing the Hash
pwned_api_check('123')