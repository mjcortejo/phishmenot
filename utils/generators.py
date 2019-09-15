import random
import string

with open('phone_prefixes.txt') as f:
    prefixes = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
prefixes = [x.strip() for x in prefixes]

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def randomInt(stringLength=10):
    numbers = "1234567890"
    return ''.join(random.choice(numbers) for i in range(stringLength))

def generate_phone_number():
    prefix = prefixes[random.randint(0, len(prefixes)-1)]
    number = f"{prefix}{randomInt(7)}"
    return number

def generate_email(fname, lname, mail, favorite_number):
    choice = random.randint(0, 3)
    domain = mail.split("@")[1]
    email = None
    if choice == 0:
        email = "{}{}@{}".format(fname, lname, domain)
    elif choice == 1:
        email = "{}_{}{}@{}".format(fname, lname, favorite_number, domain)
    elif choice == 2:
        email = "{}_{}{}@{}".format(lname, fname, favorite_number, domain)
    elif choice == 3:
        email = "{}{}@{}".format(fname, favorite_number, domain)
    email = email.lower()
    return email

def generate_user_id(fname, lname, favorite_number):
    choice = random.randint(0, 6)
    uid = None
    if choice == 0:
        uid = "{}{}".format(fname, lname)
    elif choice == 1:
        uid = "{}{}".format(fname[0], lname)
    elif choice == 2:
        uid = "{}{}".format(lname[0], fname)
    elif choice == 3:
        uid = "{}{}{}".format(fname, lname, favorite_number)
    elif choice == 4:
        uid = "{}{}{}".format(fname[0], lname, favorite_number)
    elif choice == 5:
        uid = "{}{}{}".format(lname[0], fname, favorite_number)
    elif choice == 6:
        uid = "{}{}".format(fname, favorite_number)

    uid = uid.lower()
    return uid
