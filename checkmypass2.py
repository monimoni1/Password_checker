import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
    return res


def read_res(response):
    print(response.text)




def pwned_api_check(password):
    hashed_sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_five, tail = hashed_sha1[:5], hashed_sha1[5:]
    request_api_data(first_five)
    response = request_api_data(first_five)
    print(response)
    return read_res(response)


pwned_api_check('123')
