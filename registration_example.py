import json
import os
import random

import requests

base_url = 'https://tikown.app/api'
api_key = 'TOKEN_HERE'
proxy = 'PROXY_HERE'

default_headers = {
    'x-api-key': api_key,
}


if __name__ == '__main__':
    if not proxy:
        raise Exception('Please provide proxy')

    if not api_key:
        raise Exception('Please provide api_key')

    region = 'UA'
    email = f"a1{random.randint(10, 99)}{os.urandom(3).hex()}{random.randint(10, 99)}@hotmail.com"

    print(f'{email}-{region}-{proxy}')

    birthday = f"{random.randint(1980, 2001)}-{random.randint(10, 12)}-{random.randint(10, 28)}"
    signup_body = {
        'email': email,
        'birthday': birthday,
        'password': f"{email.split('@')[0]}!",
    }

    headers = {
        'x-proxy': proxy,
        'x-region': region,
    }

    headers.update(default_headers)

    signup_result = requests.post(f'{base_url}/passport/email/signup', json=signup_body, headers=headers)

    signup_data = None
    if signup_result.status_code == 403:
        verification_data = signup_result.json()

        headers['x-device'] = json.dumps(verification_data['device'])
        headers['x-cookie'] = verification_data['cookie']

        print('Please provide verification code from mail message')
        print()

        code = input()

        verification_code_body = {
            'email': email,
            'birthday': birthday,
            'code': code,
        }

        signup_result = requests.post(f'{base_url}/passport/email/signup/check_code', json=verification_code_body, headers=headers)

        if signup_result.status_code == 200:
            signup_data = signup_result.json()
    elif signup_result.status_code != 200:
        print('Oops, something bad :(')
        print(signup_result.content)
        exit(1)

    if not signup_data:
        signup_data = signup_result.json()


    print(f'COOKIE={signup_data["cookie"]}')
    print(f'DEVICE_CONFIG={json.dumps(signup_data["device"])}')
    print(f'Tiktok account link: https://m.tiktok.com/h5/share/usr/{signup_data["response"]["data"]["user_id_str"]}.html')

