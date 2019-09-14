# https://foundation.jblfmu.edu.ph/bacolod_hr2/bdo/47ab27ed/sso/login.php?josso_back_to=https://online.bdo.com.ph/sso/josso_security_check
import random
import string

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import pandas as pd

from faker import Faker

phl_cities_df = pd.read_csv('phl_cities.csv')

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def randomInt(stringLength=10):
    numbers = "1234567890"
    return ''.join(random.choice(numbers) for i in range(stringLength))

def get_element_type(element_name, type, driver):
    element = None
    if type == 'id':
        element = driver.find_element_by_id(element_name)
    elif type == 'name':
        element = driver.find_element_by_name(element_name)
    elif type == 'xpath':
        element = driver.find_element_by_xpath(element_name)
    return element

def inputTextField(text, element_name, type, driver):
    element = get_element_type(element_name, type, driver)
    element.send_keys(text)

def clickButton(element_name, type, driver):
    element = get_element_type(element_name, type, driver)
    element.click()

def get_random_index_from_select_options(element_name, type, driver):
    element = get_element_type(element_name, type, driver)
    select = Select(element)
    max_ops_length = len(select.options)-1
    return random.randint(1, max_ops_length)

def inputSelectField(value, element_name, type, driver, select_by='text'):
    element = get_element_type(element_name, type, driver)
    select = Select(element)

    if select_by == 'index':
        select.select_by_index(value)
    elif select_by == 'text':
        select.select_by_visible_text(value)
    elif select_by == 'value':
        select.select_by_value(value)
    else:
        print("Defaulting to Visible Text")
        select.select_by_visible_text(value)

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

driver = webdriver.Chrome()

while True:
    driver.get("https://foundation.jblfmu.edu.ph/bacolod_hr2/bdo/e3c38b15/sso/login.php?josso_back_to=https://online.bdo.com.ph/sso/josso_security_check")

    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.title_contains('Banco De Oro'))
    # Login
    fake = Faker()

    fake_profile = fake.profile(fields=['mail', 'name', 'username'])
    "{'username': 'xlewis', 'name': 'Kelly Jackson', 'mail': 'sharon82@gmail.com'}"
    # print(fake_profile)

    # fake_first_name = fake.first_name()
    # fake_last_name = fake.last_name()
    fake_full_name = fake_profile['name'].split(' ')
    fake_first_name = fake_full_name[0]
    fake_last_name = fake_full_name[1]
    favorite_number = randomInt(random.randint(2,3))
    fake_email = generate_email(fake_first_name, fake_last_name, fake_profile['mail'], favorite_number)

    fake_middle_name = fake.last_name()
    fake_maiden_name = fake.last_name()

    row = random.randint(0, len(phl_cities_df)-1)
    fake_city = phl_cities_df['City'][row]
    fake_state = phl_cities_df['Province'][row]
    fake_zipcode = fake.zipcode()

    fake_credit_card = fake.credit_card_number()
    fake_security_number = fake.credit_card_security_code()

    fake_full_address = "{} {} {} {}".format(fake.street_address(), fake.building_number(), fake_city, fake_state)

    gen_user_id = generate_user_id(fake_first_name, fake_last_name, favorite_number)
    gen_password = randomString(random.randint(10,14))

    inputTextField(gen_user_id, 'channelUserID', 'name', driver)
    inputTextField(gen_password, 'channelPswdPin', 'name', driver)

    clickButton('loginButton', 'id', driver)

    #Real stuff
    account_selection = get_random_index_from_select_options('account', 'name', driver)
    inputSelectField(account_selection, 'account', 'name', driver, select_by="index")
    inputTextField(gen_user_id, 'uid', 'id', driver)
    inputTextField(gen_password, 'ps', 'id', driver)
    inputTextField(gen_password, 'cps', 'id', driver)
    inputTextField(randomInt(10), 'phoneNumber', 'id', driver)
    # inputTextField("{}{}".format(gen_user_id, domains[random.randint(0, len(domains)-1)]), 'email', 'name', driver)
    inputTextField(fake_email, 'email', 'name', driver)
    inputTextField(gen_password, 'epass', 'name', driver)
    inputTextField(fake_first_name, 'fname', 'id', driver)
    inputTextField(fake_middle_name, 'mname', 'id', driver)
    inputTextField(fake_last_name, 'lname', 'id', driver)
    inputTextField(fake_maiden_name, 'm_mname', 'name', driver)
    inputSelectField("{:02d}".format(random.randint(1,12)), 'bmonth', 'name', driver)
    inputSelectField("{:02d}".format(random.randint(1,31)), 'bdays', 'name', driver)
    inputTextField("{}".format(random.randint(1957, 2000)), 'birthyear', 'name', driver)
    inputSelectField("Social Security Number", 'ssntin', 'name', driver)
    inputTextField(randomInt(12), 'sstino', 'name', driver)
    inputTextField(fake_full_address, 'address', 'name', driver)
    inputTextField(fake_city, 'city', 'name', driver)
    inputTextField(fake_state, 'state', 'name', driver)
    inputTextField(fake_zipcode, 'zip', 'name', driver)
    q1_selection = get_random_index_from_select_options('challenge1q', 'name', driver)
    inputSelectField(q1_selection, 'challenge1q', 'name', driver, select_by="index")
    q1_answer = fake.word()
    inputTextField(q1_answer, 'ans1', 'name', driver)
    inputTextField(q1_answer, 'c_ans1', 'name', driver)
    q2_selection = get_random_index_from_select_options('challenge2q', 'name', driver)
    inputSelectField(q2_selection, 'challenge2q', 'name', driver, select_by="index")
    q2_answer = fake.word()
    inputTextField(q2_answer, 'ans2', 'name', driver)
    inputTextField(q2_answer, 'c_ans2', 'name', driver)
    inputTextField(fake_credit_card, 'cc', 'name', driver)
    exp_month = get_random_index_from_select_options('expmonth', 'name', driver)
    inputSelectField(exp_month, 'expmonth', 'name', driver, select_by="index")
    exp_year = get_random_index_from_select_options('expyear', 'name', driver)
    inputSelectField(exp_year, 'expyear', 'name', driver, select_by="index")
    inputTextField(fake_security_number, 'securitycode', 'name', driver)
    # /html/body/div[2]/div[2]/form/div[6]/div/table/tbody/tr/td[2]/select
    feedback = get_random_index_from_select_options('/html/body/div[2]/div[2]/form/div[6]/div/table/tbody/tr/td[2]/select', 'xpath', driver)
    inputSelectField(feedback, '/html/body/div[2]/div[2]/form/div[6]/div/table/tbody/tr/td[2]/select', 'xpath', driver, select_by="index")

    clickButton('submit', 'name', driver)
