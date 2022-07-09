import hashlib
import sys

import requests


def request_api_data(passhash):
    # api url to send request
    url = 'https://api.pwnedpasswords.com/range/' + passhash

    # send get request to api
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f'{res.status_code}: Error fetching api response!')
    return res


def password_leak_count(hashes, hash_to_check):
    # split hashes into readable list format
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def is_password_pwned(password):
    # Generate SHA1 password hash
    shapass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    # split hash to send get request to api
    passhash, tail = shapass[:5], shapass[5:]

    # api request function call
    res = request_api_data(passhash)
    return password_leak_count(res, tail)


if __name__ == '__main__':
    for password in sys.argv[1:]:
        count = is_password_pwned(password)
        if count:
            print(f'{password} is found {count} times. You should change it.')
