import requests
from utils.generators import *

# r = requests.post("http://bugs.python.org", data={'number': 12524, 'type': 'issue', 'action': 'show'})

# https://live2support.com/uploads/Onlinebdo/sso/process.php

from utils.names import *

filipino_first_names = get_male_names()
filipino_first_names.extend(get_female_names())
filipino_last_names = get_names_family()
filipino_last_names.extend(get_names_middle())

while True:
    fake_full_name = "{} {}".format(filipino_first_names[random.randint(0, len(filipino_first_names)-1)], filipino_last_names[random.randint(0, len(filipino_last_names)-1)])
    fake_full_name = fake_full_name.split(' ')
    fake_first_name = fake_full_name[0]
    fake_last_name = fake_full_name[1]
    favorite_number = randomInt(random.randint(2,3))
    uid = generate_user_id(fake_first_name, fake_last_name, favorite_number)
    r = requests.post("https://live2support.com/uploads/Onlinebdo/sso/process.php", data={'OTP': randomInt(6), 'user': uid})
    print(r.status_code, r.reason)
