import hashlib
import requests
import sys

def request_api_data(query):
    url = 'https://api.pwnedpasswords.com/range/' + query
    res = requests.get(url)
    if res.status_code != 200:
        print(f'Error: Api request was not successful. error code {res.status_code}')
    else:
        return res


def get_passwords_leak_count(hashes, hash_to_check):
    hashes= (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
     if h == hash_to_check:
         return count
    return 0

def pwned_api_check(password):
    hashed_sha1= hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_five , tail = hashed_sha1[:5] , hashed_sha1[5:]
    response = request_api_data(first_five)
    print(response)
    return get_passwords_leak_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'your password {password} was found {count} times... you shoould change your password')
        else:
            print(f'{password} was not found congrats. Carry on')
    return 'Done!'


main(sys.argv[1:])
